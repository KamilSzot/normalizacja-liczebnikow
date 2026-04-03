"""Main normalization function for Polish number normalizer."""

import re
from src.parser import parse_compound
from src.mappings import lookup_word, is_thousand_word, ORDINAL


def normalize_polish_numbers(text: str) -> str:
    """Replace Polish number words with digits in text.
    
    Args:
        text: Input text possibly containing Polish number words
        
    Returns:
        Text with Polish number words replaced by digits
    """
    if not text:
        return text
    
    # Tokenize: find all word tokens with their positions
    tokens = []
    for m in re.finditer(r'\w+', text):
        tokens.append((m.start(), m.end(), m.group()))
    
    if not tokens:
        return text
    
    # Find all number matches using greedy longest match
    matches = []  # list of (start_token_idx, end_token_idx, value)
    consumed = set()  # indices of tokens already part of a match
    
    i = 0
    while i < len(tokens):
        if i in consumed:
            i += 1
            continue
        
        # Try longest possible compound starting at position i
        best_match = None
        
        # Maximum lookahead: up to 12 words (for long compounds like
        # "dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć")
        max_len = min(12, len(tokens) - i)
        
        for length in range(max_len, 0, -1):
            # Check if any token in this range is already consumed
            if any((i + j) in consumed for j in range(length)):
                continue

            if not _tokens_are_whitespace_separated(text, tokens, i, i + length):
                continue
            
            # Extract words for this span
            words = [tokens[i + j][2] for j in range(length)]
            
            # Try to parse as compound
            value = parse_compound(words)
            if value is not None:
                if _should_defer_match_to_next_token(text, tokens, i, i + length):
                    continue
                best_match = (i, i + length, value)
                break  # Found longest match
        
        if best_match is not None:
            start_idx, end_idx, value = best_match
            matches.append((start_idx, end_idx, value))
            for j in range(start_idx, end_idx):
                consumed.add(j)
            i = end_idx
        else:
            i += 1
    
    if not matches:
        return text
    
    # Build result string by replacing matches from left to right
    result_parts = []
    cursor = 0
    previous_was_match = False
    
    for start_idx, end_idx, value in matches:
        # Text before this match
        match_start = tokens[start_idx][0]
        match_end = tokens[end_idx - 1][1]
        
        if cursor < match_start:
            gap = text[cursor:match_start]
            if previous_was_match and gap.isspace():
                result_parts.append(' ')
            else:
                result_parts.append(gap)
        
        result_parts.append(str(value))
        cursor = match_end
        previous_was_match = True
    
    # Remaining text after last match
    if cursor < len(text):
        result_parts.append(text[cursor:])
    
    return ''.join(result_parts)


def _tokens_are_whitespace_separated(
    text: str,
    tokens: list[tuple[int, int, str]],
    start_idx: int,
    end_idx: int,
) -> bool:
    """Only allow compounds built from tokens separated by whitespace."""
    for idx in range(start_idx, end_idx - 1):
        gap = text[tokens[idx][1]:tokens[idx + 1][0]]
        if not gap.isspace():
            return False
    return True


def _should_defer_match_to_next_token(
    text: str,
    tokens: list[tuple[int, int, str]],
    start_idx: int,
    end_idx: int,
) -> bool:
    """Avoid consuming an incomplete tail when the next token continues the number."""
    if end_idx >= len(tokens):
        return False

    next_gap = text[tokens[end_idx - 1][1]:tokens[end_idx][0]]
    if not next_gap.isspace():
        return False

    next_info = lookup_word(tokens[end_idx][2])
    if next_info is None:
        return False

    next_value, next_category = next_info
    if next_category != ORDINAL and not is_thousand_word(tokens[end_idx][2]):
        return False

    span_infos = [lookup_word(tokens[idx][2]) for idx in range(start_idx, end_idx)]
    if any(info is None for info in span_infos):
        return False

    has_thousand = any(info[1] != ORDINAL and is_thousand_word(tokens[start_idx + offset][2]) for offset, info in enumerate(span_infos))
    last_value, last_category = span_infos[-1]

    if is_thousand_word(tokens[end_idx][2]) and has_thousand and last_category != ORDINAL:
        return last_category in {'unit', 'teen', 'ten', 'hundred'}

    if next_category == ORDINAL and last_category == ORDINAL:
        return True

    return False
