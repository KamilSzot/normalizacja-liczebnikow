"""Polish diacritic handling utilities."""

import re

DIACRITIC_MAP = {
    'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
    'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
    'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
    'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z',
}

_DIACRITIC_TABLE = str.maketrans(DIACRITIC_MAP)


def remove_diacritics(text: str) -> str:
    """Remove Polish diacritics from text."""
    return text.translate(_DIACRITIC_TABLE)


def normalize_for_comparison(text: str) -> str:
    """Normalize text for comparison purposes.
    
    - Removes Polish diacritics
    - Lowercases all characters
    - Removes punctuation except period, comma and question mark
    - Deduplicates punctuation leaving last
    - Removes whitespace before retained punctuation
    - Deduplicates whitespace
    - Trims whitespace from beginning and end
    - Strips punctuation from beginning and end
    """
    text = remove_diacritics(text)
    text = text.lower()
    text = re.sub(r'[^\w\s.,?]', '', text)
    text = re.sub(r'([.,?])+', r'\1', text)
    text = re.sub(r'\s+([.,?])', r'\1', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    text = text.lstrip('.,?')
    text = text.rstrip('.,')
    return text
