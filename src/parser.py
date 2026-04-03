"""Compound number parser for Polish number normalizer."""

from src.mappings import (
    lookup_word, get_thousand_type,
    UNIT, TEEN, TEN, HUNDRED, THOUSAND, ORDINAL,
)


def parse_compound(words: list[str]) -> int | None:
    """Parse a list of words as a compound Polish number.
    
    Returns the numeric value, or None if not a valid compound.
    """
    if not words:
        return None

    # Look up all words first
    infos: list[tuple[int, str] | None] = []
    for w in words:
        info = lookup_word(w)
        if info is None:
            return None
        infos.append(info)

    n = len(infos)

    if all(cat == ORDINAL for _, cat in infos):
        return _parse_ordinal_compound([value for value, _ in infos])

    first_ordinal_idx = next((idx for idx, (_, cat) in enumerate(infos) if cat == ORDINAL), None)
    if first_ordinal_idx is not None:
        if not all(cat == ORDINAL for _, cat in infos[first_ordinal_idx:]):
            return None

        prefix_value = 0
        if first_ordinal_idx > 0:
            prefix_value = _parse_cardinal_compound(words[:first_ordinal_idx], infos[:first_ordinal_idx])
            if prefix_value is None:
                return None

        ordinal_tail_value = _parse_ordinal_compound([value for value, _ in infos[first_ordinal_idx:]])
        if ordinal_tail_value is None:
            return None

        return prefix_value + ordinal_tail_value
    
    return _parse_cardinal_compound(words, infos)


def _parse_cardinal_compound(
    words: list[str],
    infos: list[tuple[int, str]],
) -> int | None:
    """Parse a sequence containing only cardinal/thousand forms."""
    n = len(infos)

    # Single word
    if n == 1:
        val, cat = infos[0]
        if cat == THOUSAND:
            ttype = get_thousand_type(words[0])
            if ttype == 'singular':
                return 1000
            if ttype == 'plural_loc':
                return 2000
            # Other plural forms can't stand alone
            return None
        return val

    total = 0       # Accumulated total from thousand-level processing
    current = 0     # Current sub-total being built
    had_thousand = False
    # Track what was last added to current:
    # None, 'unit', 'teen', 'ten', 'hundred', 'thousand'
    last_added = None

    for i in range(n):
        val, cat = infos[i]
        word = words[i]

        if cat == ORDINAL:
            # Ordinal: only valid as sole word, or after thousand (thousand-level ordinal)
            if i == 0 and n == 1:
                return val
            if had_thousand and i == n - 1 and last_added == 'thousand' and val >= 1000:
                return total + val
            return None

        if cat == THOUSAND:
            if had_thousand:
                return None  # No double thousand

            ttype = get_thousand_type(word)

            if current == 0:
                # Standalone thousand
                if ttype == 'singular':
                    total = 1000
                elif ttype == 'plural_loc':
                    total = 2000
                else:
                    return None  # Other plural forms can't stand alone
            else:
                # Multiplier + thousand
                if ttype == 'singular':
                    return None  # Singular can't have multiplier
                if _valid_thousand_agreement(current, ttype):
                    total = current * 1000
                else:
                    return None

            had_thousand = True
            current = 0
            last_added = 'thousand'
            continue

        # Non-thousand, non-ordinal word
        if cat == HUNDRED:
            if last_added in (None, 'thousand'):
                current += val
                last_added = 'hundred'
            else:
                return None  # Can't add hundred after other sub-components

        elif cat == TEN:
            if last_added in (None, 'thousand', 'hundred'):
                current += val
                last_added = 'ten'
            else:
                return None  # Can't add ten after unit/teen/ten

        elif cat == TEEN:
            if last_added in (None, 'thousand', 'hundred'):
                current += val
                last_added = 'teen'
            else:
                return None  # Can't add teen after unit/teen/ten

        elif cat == UNIT:
            if last_added in (None, 'thousand', 'hundred', 'ten'):
                current += val
                last_added = 'unit'
            else:
                return None  # Can't add unit after unit/teen

    return total + current


def _parse_ordinal_compound(values: list[int]) -> int | None:
    """Parse multi-word ordinal sequences like 'dwudziesty piąty'."""
    total = 0
    current = 0
    last_added = None

    for value in values:
        category = _ordinal_value_category(value)

        if category == THOUSAND:
            if current == 0:
                current = value
            else:
                current *= 1000
            last_added = 'thousand'
            total += current
            current = 0
            continue

        if category == HUNDRED:
            if last_added in (None, 'thousand'):
                current += value
                last_added = 'hundred'
            else:
                return None
            continue

        if category == TEN:
            if last_added in (None, 'thousand', 'hundred'):
                current += value
                last_added = 'ten'
            else:
                return None
            continue

        if category == TEEN:
            if last_added in (None, 'thousand', 'hundred'):
                current += value
                last_added = 'teen'
            else:
                return None
            continue

        if category == UNIT:
            if last_added in (None, 'thousand', 'hundred', 'ten'):
                current += value
                last_added = 'unit'
            else:
                return None
            continue

        return None

    return total + current


def _ordinal_value_category(value: int) -> str | None:
    """Map an ordinal numeric value to the same composition buckets as cardinals."""
    if value == 1000 or (value > 1000 and value % 1000 == 0):
        return THOUSAND
    if 100 <= value <= 900 and value % 100 == 0:
        return HUNDRED
    if 20 <= value <= 90 and value % 10 == 0:
        return TEN
    if 10 <= value <= 19:
        return TEEN
    if 1 <= value <= 9:
        return UNIT
    return None


def _valid_thousand_agreement(multiplier: int, ttype: str) -> bool:
    """Check if the multiplier value agrees with the thousand word type."""
    if ttype == 'singular':
        return False  # Singular stands alone
    if ttype == 'plural_nom_acc':
        # tysiące: valid for 2-4 (by last digit, excluding 12-14)
        last_digit = multiplier % 10
        last_two = multiplier % 100
        return last_digit in {2, 3, 4} and last_two not in {12, 13, 14}
    # tysięcy, tysiącami, tysiącom, tysiącach: valid for 2+
    return multiplier >= 2
