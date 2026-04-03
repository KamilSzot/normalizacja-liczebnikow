"""Number word mappings for Polish number normalizer."""

from normalizacja_liczebnikow.diacritics import remove_diacritics

# Categories for number words
UNIT = 'unit'        # 1-9
TEEN = 'teen'        # 10-19
TEN = 'ten'          # 20-90
HUNDRED = 'hundred'  # 100-900
THOUSAND = 'thousand'  # tysiąc/tysiące/tysięcy etc.
ORDINAL = 'ordinal'  # ordinal numbers


def _value_to_category(value: int) -> str:
    """Determine the category of a cardinal number based on its value."""
    if 1 <= value <= 9:
        return UNIT
    elif 10 <= value <= 19:
        return TEEN
    elif 20 <= value <= 90 and value % 10 == 0:
        return TEN
    elif 100 <= value <= 900 and value % 100 == 0:
        return HUNDRED
    else:
        return UNIT  # fallback


# All cardinal number forms organized by case
# Each entry: value -> list of word forms
CARDINAL_FORMS = {
    # === 0-19 ===
    0: {
        'nominative': ['zero'],
        'genitive': ['zera'],
        'accusative': ['zero'],
        'instrumental': ['zerem'],
        'locative': ['zerze'],
        'vocative': ['zero'],
        'adjective': ['zerowa', 'zerowy', 'zerowe'],
    },
    1: {
        'nominative': ['jeden', 'jedna', 'jedno'],
        'genitive': ['jednego'],
        'dative': ['jednemu'],
        'accusative': ['jednego'],  # masculine accusative = genitive
        'instrumental': ['jednym'],
        'feminine_accusative': ['jedną'],
        'feminine_instrumental': ['jedną'],
    },
    2: {
        'nominative': ['dwa', 'dwaj', 'dwie'],
        'genitive': ['dwóch'],
        'dative': ['dwóm', 'dwu'],
        'accusative': ['dwa', 'dwie'],
        'instrumental': ['dwoma'],
    },
    3: {
        'nominative': ['trzy', 'trzej'],
        'genitive': ['trzech'],
        'dative': ['trzem'],
        'accusative': ['trzy'],
        'instrumental': ['trzema'],
    },
    4: {
        'nominative': ['cztery', 'czterej'],
        'genitive': ['czterech'],
        'dative': ['czterem'],
        'accusative': ['cztery'],
        'instrumental': ['czterema'],
    },
    5: {
        'nominative': ['pięć'],
        'genitive': ['pięciu'],
        'dative': ['pięciu'],
        'accusative': ['pięć'],
        'instrumental': ['pięcioma'],
    },
    6: {
        'nominative': ['sześć'],
        'genitive': ['sześciu'],
        'dative': ['sześciu'],
        'accusative': ['sześć'],
        'instrumental': ['sześcioma'],
    },
    7: {
        'nominative': ['siedem'],
        'genitive': ['siedmiu'],
        'dative': ['siedmiu'],
        'accusative': ['siedem'],
        'instrumental': ['siedmioma'],
    },
    8: {
        'nominative': ['osiem'],
        'genitive': ['ośmiu'],
        'dative': ['ośmiu'],
        'accusative': ['osiem'],
        'instrumental': ['ośmioma'],
    },
    9: {
        'nominative': ['dziewięć'],
        'genitive': ['dziewięciu'],
        'dative': ['dziewięciu'],
        'accusative': ['dziewięć'],
        'instrumental': ['dziewięcioma'],
    },
    10: {
        'nominative': ['dziesięć'],
        'genitive': ['dziesięciu'],
        'dative': ['dziesięciu'],
        'accusative': ['dziesięć'],
        'instrumental': ['dziesięcioma'],
    },
    11: {
        'nominative': ['jedenaście'],
        'genitive': ['jedenastu'],
        'dative': ['jedenastu'],
        'accusative': ['jedenaście'],
        'instrumental': ['jedenastoma'],
    },
    12: {
        'nominative': ['dwanaście'],
        'genitive': ['dwunastu'],
        'dative': ['dwunastu'],
        'accusative': ['dwanaście'],
        'instrumental': ['dwunastoma'],
    },
    13: {
        'nominative': ['trzynaście'],
        'genitive': ['trzynastu'],
        'dative': ['trzynastu'],
        'accusative': ['trzynaście'],
        'instrumental': ['trzynastoma'],
    },
    14: {
        'nominative': ['czternaście'],
        'genitive': ['czternastu'],
        'dative': ['czternastu'],
        'accusative': ['czternaście'],
        'instrumental': ['czternastoma'],
    },
    15: {
        'nominative': ['piętnaście'],
        'genitive': ['piętnastu'],
        'dative': ['piętnastu'],
        'accusative': ['piętnaście'],
        'instrumental': ['piętnastoma'],
    },
    16: {
        'nominative': ['szesnaście'],
        'genitive': ['szesnastu'],
        'dative': ['szesnastu'],
        'accusative': ['szesnaście'],
        'instrumental': ['szesnastoma'],
    },
    17: {
        'nominative': ['siedemnaście'],
        'genitive': ['siedemnastu'],
        'dative': ['siedemnastu'],
        'accusative': ['siedemnaście'],
        'instrumental': ['siedemnastoma'],
    },
    18: {
        'nominative': ['osiemnaście'],
        'genitive': ['osiemnastu'],
        'dative': ['osiemnastu'],
        'accusative': ['osiemnaście'],
        'instrumental': ['osiemnastoma'],
    },
    19: {
        'nominative': ['dziewiętnaście'],
        'genitive': ['dziewiętnastu'],
        'dative': ['dziewiętnastu'],
        'accusative': ['dziewiętnaście'],
        'instrumental': ['dziewiętnastoma'],
    },
    # === Tens 20-90 ===
    20: {
        'nominative': ['dwadzieścia'],
        'genitive': ['dwudziestu'],
        'dative': ['dwudziestu'],
        'accusative': ['dwadzieścia'],
        'instrumental': ['dwudziestoma'],
    },
    30: {
        'nominative': ['trzydzieści'],
        'genitive': ['trzydziestu'],
        'dative': ['trzydziestu'],
        'accusative': ['trzydzieści'],
        'instrumental': ['trzydziestoma'],
    },
    40: {
        'nominative': ['czterdzieści'],
        'genitive': ['czterdziestu'],
        'dative': ['czterdziestu'],
        'accusative': ['czterdzieści'],
        'instrumental': ['czterdziestoma'],
    },
    50: {
        'nominative': ['pięćdziesiąt'],
        'genitive': ['pięćdziesięciu'],
        'dative': ['pięćdziesięciu'],
        'accusative': ['pięćdziesiąt'],
        'instrumental': ['pięćdziesięcioma'],
    },
    60: {
        'nominative': ['sześćdziesiąt'],
        'genitive': ['sześćdziesięciu'],
        'dative': ['sześćdziesięciu'],
        'accusative': ['sześćdziesiąt'],
        'instrumental': ['sześćdziesięcioma'],
    },
    70: {
        'nominative': ['siedemdziesiąt'],
        'genitive': ['siedemdziesięciu'],
        'dative': ['siedemdziesięciu'],
        'accusative': ['siedemdziesiąt'],
        'instrumental': ['siedemdziesięcioma'],
    },
    80: {
        'nominative': ['osiemdziesiąt'],
        'genitive': ['osiemdziesięciu'],
        'dative': ['osiemdziesięciu'],
        'accusative': ['osiemdziesiąt'],
        'instrumental': ['osiemdziesięcioma'],
    },
    90: {
        'nominative': ['dziewięćdziesiąt'],
        'genitive': ['dziewięćdziesięciu'],
        'dative': ['dziewięćdziesięciu'],
        'accusative': ['dziewięćdziesiąt'],
        'instrumental': ['dziewięćdziesięcioma'],
    },
    # === Hundreds 100-900 ===
    100: {
        'nominative': ['sto'],
        'genitive': ['stu'],
        'dative': ['stu'],
        'accusative': ['sto'],
        'instrumental': ['stu'],
    },
    200: {
        'nominative': ['dwieście'],
        'genitive': ['dwustu'],
        'dative': ['dwustu'],
        'accusative': ['dwieście'],
        'instrumental': ['dwustoma'],
    },
    300: {
        'nominative': ['trzysta'],
        'genitive': ['trzystu'],
        'dative': ['trzystu'],
        'accusative': ['trzysta'],
        'instrumental': ['trzystoma'],
    },
    400: {
        'nominative': ['czterysta'],
        'genitive': ['czterystu'],
        'dative': ['czterystu'],
        'accusative': ['czterysta'],
        'instrumental': ['czterystoma'],
    },
    500: {
        'nominative': ['pięćset'],
        'genitive': ['pięciuset'],
        'dative': ['pięciuset'],
        'accusative': ['pięćset'],
        'instrumental': ['pięciuset'],
    },
    600: {
        'nominative': ['sześćset'],
        'genitive': ['sześciuset'],
        'dative': ['sześciuset'],
        'accusative': ['sześćset'],
        'instrumental': ['sześciuset'],
    },
    700: {
        'nominative': ['siedemset'],
        'genitive': ['siedmiuset'],
        'dative': ['siedmiuset'],
        'accusative': ['siedemset'],
        'instrumental': ['siedmiuset'],
    },
    800: {
        'nominative': ['osiemset'],
        'genitive': ['ośmiuset'],
        'dative': ['ośmiuset'],
        'accusative': ['osiemset'],
        'instrumental': ['ośmiuset'],
    },
    900: {
        'nominative': ['dziewięćset'],
        'genitive': ['dziewięciuset'],
        'dative': ['dziewięciuset'],
        'accusative': ['dziewięćset'],
        'instrumental': ['dziewięciuset'],
    },
}

# Thousand-word forms
# These are the words that mean "thousand" in various cases
# value 1000 is the base, the actual multiplier comes from context
THOUSAND_FORMS = {
    'singular': ['tysiąc', 'tysiąca', 'tysiącem', 'tysiącu', 'tysiącowi'],
    'plural_nom_acc': ['tysiące'],  # 2-4 thousand (nominative/accusative)
    'plural_gen': ['tysięcy'],       # 5+ thousand (genitive)
    'plural_inst': ['tysiącami'],    # instrumental plural
    'plural_dat': ['tysiącom'],      # dative plural
    'plural_loc': ['tysiącach'],     # locative plural
}

# Ordinal number forms
ORDINAL_FORMS = {
    # 1st-19th: masculine, feminine, neuter
    1: ['pierwszy', 'pierwsza', 'pierwsze'],
    2: ['drugi', 'druga', 'drugie'],
    3: ['trzeci', 'trzecia', 'trzecie'],
    4: ['czwarty', 'czwarta', 'czwarte'],
    5: ['piąty', 'piąta', 'piąte'],
    6: ['szósty', 'szósta', 'szóste'],
    7: ['siódmy', 'siódma', 'siódme'],
    8: ['ósmy', 'ósma', 'ósme'],
    9: ['dziewiąty', 'dziewiąta', 'dziewiąte'],
    10: ['dziesiąty', 'dziesiąta', 'dziesiąte'],
    11: ['jedenasty', 'jedenasta', 'jedenaste'],
    12: ['dwunasty', 'dwunasta', 'dwunaste'],
    13: ['trzynasty', 'trzynasta', 'trzynaste'],
    14: ['czternasty', 'czternasta', 'czternaste'],
    15: ['piętnasty', 'piętnasta', 'piętnaste'],
    16: ['szesnasty', 'szesnasta', 'szesnaste'],
    17: ['siedemnasty', 'siedemnasta', 'siedemnaste'],
    18: ['osiemnasty', 'osiemnasta', 'osiemnaste'],
    19: ['dziewiętnasty', 'dziewiętnasta', 'dziewiętnaste'],
    # Tens 20th-90th
    20: ['dwudziesty', 'dwudziesta', 'dwudzieste'],
    30: ['trzydziesty', 'trzydziesta', 'trzydzieste'],
    40: ['czterdziesty', 'czterdziesta', 'czterdzieste'],
    50: ['pięćdziesiąty', 'pięćdziesiąta', 'pięćdziesiąte'],
    60: ['sześćdziesiąty', 'sześćdziesiąta', 'sześćdziesiąte'],
    70: ['siedemdziesiąty', 'siedemdziesiąta', 'siedemdziesiąte'],
    80: ['osiemdziesiąty', 'osiemdziesiąta', 'osiemdziesiąte'],
    90: ['dziewięćdziesiąty', 'dziewięćdziesiąta', 'dziewięćdziesiąte'],
    # Hundreds 100th-900th
    100: ['setny', 'setna', 'setne'],
    200: ['dwusetny', 'dwuseta', 'dwusete', 'dwóchsetny', 'dwóchsetna', 'dwóchsetne'],
    300: ['trzechsetny', 'trzechsetna', 'trzechsetne'],
    400: ['czterechsetny', 'czterechsetna', 'czterechsetne'],
    500: ['pięćsetny', 'pięćsetna', 'pięćsetne'],
    600: ['sześćsetny', 'sześćsetna', 'sześćsetne'],
    700: ['siedemsetny', 'siedemsetna', 'siedemsetne'],
    800: ['osiemsetny', 'osiemsetna', 'osiemsetne'],
    900: ['dziewięćsetny', 'dziewięćsetna', 'dziewięćsetne'],
    # Thousands 1000th-9000th (single-word forms)
    1000: ['tysięczny', 'tysięczna', 'tysięczne'],
    2000: ['dwutysięczny', 'dwutysięczna', 'dwutysięczne'],
    3000: ['trzytysięczny', 'trzytysięczna', 'trzytysięczne'],
    4000: ['cztertysięczny', 'cztertysięczna', 'cztertysięczne'],
    5000: ['pięciotysięczny', 'pięciotysięczna', 'pięciotysięczne'],
    6000: ['sześciotysięczny', 'sześciotysięczna', 'sześciotysięczne'],
    7000: ['siedmiotysięczny', 'siedmiotysięczna', 'siedmiotysięczne'],
    8000: ['ośmiotysięczny', 'ośmiotysięczna', 'ośmiotysięczne'],
    9000: ['dziewięciotysięczny', 'dziewięciotysięczna', 'dziewięciotysięczne'],
    # Ten thousands 10000th-90000th (single-word forms)
    10000: ['dziesięciotysięczny', 'dziesięciotysięczna', 'dziesięciotysięczne'],
    20000: ['dwudziestotysięczny', 'dwudziestotysięczna', 'dwudziestotysięczne'],
    30000: ['trzydziestotysięczny', 'trzydziestotysięczna', 'trzydziestotysięczne'],
    40000: ['czterdziestotysięczny', 'czterdziestotysięczna', 'czterdziestotysięczne'],
    50000: ['pięćdziesięciotysięczny', 'pięćdziesięciotysięczna', 'pięćdziesięciotysięczne'],
    60000: ['sześćdziesięciotysięczny', 'sześćdziesięciotysięczna', 'sześćdziesięciotysięczne'],
    70000: ['siedemdziesięciotysięczny', 'siedemdziesięciotysięczna', 'siedemdziesięciotysięczne'],
    80000: ['osiemdziesięciotysięczny', 'osiemdziesięciotysięczna', 'osiemdziesięciotysięczne'],
    90000: ['dziewięćdziesięciotysięczny', 'dziewięćdziesięciotysięczna', 'dziewięćdziesięciotysięczne'],
}

# Compound ordinal forms (multi-word)
COMPOUND_ORDINAL_FORMS = {
    25000: ['dwudziestopięciotysięczny', 'dwudziestopięciotysięczna', 'dwudziestopięciotysięczne'],
}


# Additional declined ordinal forms from common adjective-like inflection.
ORDINAL_DECLINED_FORMS = {
    1: ['pierwszego', 'pierwszemu', 'pierwszym', 'pierwszej', 'pierwsz\u0105', 'pierwszych', 'pierwszymi'],
    2: ['drugiego', 'drugiemu', 'drugim', 'drugiej', 'drug\u0105', 'drugich', 'drugimi'],
    3: ['trzeciego', 'trzeciemu', 'trzecim', 'trzeciej', 'trzeci\u0105', 'trzecich', 'trzecimi'],
    4: ['czwartego', 'czwartemu', 'czwartym', 'czwartej', 'czwart\u0105', 'czwartych', 'czwartymi'],
    5: ['pi\u0105tego', 'pi\u0105temu', 'pi\u0105tym', 'pi\u0105tej', 'pi\u0105t\u0105', 'pi\u0105tych', 'pi\u0105tymi'],
    6: ['sz\u00f3stego', 'sz\u00f3stemu', 'sz\u00f3stym', 'sz\u00f3stej', 'sz\u00f3st\u0105', 'sz\u00f3stych', 'sz\u00f3stymi'],
    7: ['si\u00f3dmego', 'si\u00f3dmemu', 'si\u00f3dmym', 'si\u00f3dmej', 'si\u00f3dm\u0105', 'si\u00f3dmych', 'si\u00f3dmymi'],
    8: ['\u00f3smego', '\u00f3smemu', '\u00f3smym', '\u00f3smej', '\u00f3sm\u0105', '\u00f3smych', '\u00f3smymi'],
    9: ['dziewi\u0105tego', 'dziewi\u0105temu', 'dziewi\u0105tym', 'dziewi\u0105tej', 'dziewi\u0105t\u0105', 'dziewi\u0105tych', 'dziewi\u0105tymi'],
    10: ['dziesi\u0105tego', 'dziesi\u0105temu', 'dziesi\u0105tym', 'dziesi\u0105tej', 'dziesi\u0105t\u0105', 'dziesi\u0105tych', 'dziesi\u0105tymi'],
    20: ['dwudziestego', 'dwudziestemu', 'dwudziestym', 'dwudziestej', 'dwudziest\u0105', 'dwudziestych', 'dwudziestymi'],
    30: ['trzydziestego', 'trzydziestemu', 'trzydziestym', 'trzydziestej', 'trzydziest\u0105', 'trzydziestych', 'trzydziestymi'],
}

# ============================================================
# Build lookup dictionaries
# ============================================================

# Main lookup: normalized word (lowercase, with diacritics) -> (value, category)
WORD_TO_INFO: dict[str, tuple[int, str]] = {}

# Non-diacritic lookup: word without diacritics -> (value, category)
WORD_TO_INFO_NODIA: dict[str, tuple[int, str]] = {}

# Thousand word set for quick lookup
THOUSAND_WORDS: set[str] = set()

# Singular thousand words (standalone = 1000)
SINGULAR_THOUSAND_WORDS: set[str] = set()

# Plural thousand words that require 2-4 multiplier (tysiące)
PLURAL_NOM_ACC_THOUSAND: set[str] = set()

# Plural thousand words that require 2+ multiplier
PLURAL_GEN_THOUSAND: set[str] = set()
PLURAL_INST_THOUSAND: set[str] = set()
PLURAL_DAT_THOUSAND: set[str] = set()
PLURAL_LOC_THOUSAND: set[str] = set()


def _add_word(word: str, value: int, category: str) -> None:
    """Add a word to both lookup dictionaries."""
    key = word.lower()
    WORD_TO_INFO[key] = (value, category)
    nodia_key = remove_diacritics(word).lower()
    # Only add non-diacritic key if it's different
    if nodia_key != key:
        WORD_TO_INFO_NODIA[nodia_key] = (value, category)


def _build_lookups() -> None:
    """Build all lookup dictionaries from the source data."""
    # Cardinal forms
    for value, cases in CARDINAL_FORMS.items():
        category = _value_to_category(value)
        for case_name, words in cases.items():
            for word in words:
                _add_word(word, value, category)

    # Thousand words
    for word in THOUSAND_FORMS['singular']:
        key = word.lower()
        THOUSAND_WORDS.add(key)
        SINGULAR_THOUSAND_WORDS.add(key)
        WORD_TO_INFO[key] = (1000, THOUSAND)
        nodia = remove_diacritics(word).lower()
        if nodia != key:
            THOUSAND_WORDS.add(nodia)
            SINGULAR_THOUSAND_WORDS.add(nodia)
            WORD_TO_INFO_NODIA[nodia] = (1000, THOUSAND)

    for word in THOUSAND_FORMS['plural_nom_acc']:
        key = word.lower()
        THOUSAND_WORDS.add(key)
        PLURAL_NOM_ACC_THOUSAND.add(key)
        WORD_TO_INFO[key] = (1000, THOUSAND)
        nodia = remove_diacritics(word).lower()
        if nodia != key:
            THOUSAND_WORDS.add(nodia)
            PLURAL_NOM_ACC_THOUSAND.add(nodia)
            WORD_TO_INFO_NODIA[nodia] = (1000, THOUSAND)

    for word in THOUSAND_FORMS['plural_gen']:
        key = word.lower()
        THOUSAND_WORDS.add(key)
        PLURAL_GEN_THOUSAND.add(key)
        WORD_TO_INFO[key] = (1000, THOUSAND)
        nodia = remove_diacritics(word).lower()
        if nodia != key:
            THOUSAND_WORDS.add(nodia)
            PLURAL_GEN_THOUSAND.add(nodia)
            WORD_TO_INFO_NODIA[nodia] = (1000, THOUSAND)

    for word in THOUSAND_FORMS['plural_inst']:
        key = word.lower()
        THOUSAND_WORDS.add(key)
        PLURAL_INST_THOUSAND.add(key)
        WORD_TO_INFO[key] = (1000, THOUSAND)
        nodia = remove_diacritics(word).lower()
        if nodia != key:
            THOUSAND_WORDS.add(nodia)
            PLURAL_INST_THOUSAND.add(nodia)
            WORD_TO_INFO_NODIA[nodia] = (1000, THOUSAND)

    for word in THOUSAND_FORMS['plural_dat']:
        key = word.lower()
        THOUSAND_WORDS.add(key)
        PLURAL_DAT_THOUSAND.add(key)
        WORD_TO_INFO[key] = (1000, THOUSAND)
        nodia = remove_diacritics(word).lower()
        if nodia != key:
            THOUSAND_WORDS.add(nodia)
            PLURAL_DAT_THOUSAND.add(nodia)
            WORD_TO_INFO_NODIA[nodia] = (1000, THOUSAND)

    for word in THOUSAND_FORMS['plural_loc']:
        key = word.lower()
        THOUSAND_WORDS.add(key)
        PLURAL_LOC_THOUSAND.add(key)
        WORD_TO_INFO[key] = (1000, THOUSAND)
        nodia = remove_diacritics(word).lower()
        if nodia != key:
            THOUSAND_WORDS.add(nodia)
            PLURAL_LOC_THOUSAND.add(nodia)
            WORD_TO_INFO_NODIA[nodia] = (1000, THOUSAND)

    # Ordinal forms
    for value, words in ORDINAL_FORMS.items():
        for word in words:
            _add_word(word, value, ORDINAL)

    for value, words in ORDINAL_DECLINED_FORMS.items():
        for word in words:
            _add_word(word, value, ORDINAL)

    # Compound ordinal forms
    for value, words in COMPOUND_ORDINAL_FORMS.items():
        for word in words:
            _add_word(word, value, ORDINAL)


# Build on module load
_build_lookups()


def lookup_word(word: str) -> tuple[int, str] | None:
    """Look up a word in the dictionaries. Returns (value, category) or None."""
    key = word.lower()
    if key in WORD_TO_INFO:
        return WORD_TO_INFO[key]
    nodia = remove_diacritics(key)
    if nodia in WORD_TO_INFO_NODIA:
        return WORD_TO_INFO_NODIA[nodia]
    return None


def is_thousand_word(word: str) -> bool:
    """Check if a word is a thousand-word form."""
    key = word.lower()
    if key in THOUSAND_WORDS:
        return True
    nodia = remove_diacritics(key)
    return nodia in THOUSAND_WORDS


def get_thousand_type(word: str) -> str | None:
    """Get the type of thousand word: 'singular', 'plural_nom_acc', 'plural_gen', etc."""
    key = word.lower()
    # Check with diacritics first
    if key in SINGULAR_THOUSAND_WORDS:
        return 'singular'
    if key in PLURAL_NOM_ACC_THOUSAND:
        return 'plural_nom_acc'
    if key in PLURAL_GEN_THOUSAND:
        return 'plural_gen'
    if key in PLURAL_INST_THOUSAND:
        return 'plural_inst'
    if key in PLURAL_DAT_THOUSAND:
        return 'plural_dat'
    if key in PLURAL_LOC_THOUSAND:
        return 'plural_loc'
    # Try without diacritics
    nodia = remove_diacritics(key)
    if nodia in SINGULAR_THOUSAND_WORDS:
        return 'singular'
    if nodia in PLURAL_NOM_ACC_THOUSAND:
        return 'plural_nom_acc'
    if nodia in PLURAL_GEN_THOUSAND:
        return 'plural_gen'
    if nodia in PLURAL_INST_THOUSAND:
        return 'plural_inst'
    if nodia in PLURAL_DAT_THOUSAND:
        return 'plural_dat'
    if nodia in PLURAL_LOC_THOUSAND:
        return 'plural_loc'
    return None


def valid_thousand_agreement(multiplier: int, thousand_word: str) -> bool:
    """Check if the multiplier value agrees with the thousand word form."""
    ttype = get_thousand_type(thousand_word)
    if ttype is None:
        return False
    if ttype == 'singular':
        # Singular forms (tysiąc, tysiąca, etc.) stand alone as 1000
        # They should NOT be preceded by a multiplier in a compound
        return False
    if ttype == 'plural_nom_acc':
        # tysiące: valid for 2-4 (by last digit, excluding 12-14)
        last_digit = multiplier % 10
        last_two = multiplier % 100
        return last_digit in {2, 3, 4} and last_two not in {12, 13, 14}
    if ttype == 'plural_loc':
        # tysiącach: valid for 2+ (standalone defaults to 2000)
        return multiplier >= 2
    # tysięcy, tysiącami, tysiącom: valid for 2+
    return multiplier >= 2
