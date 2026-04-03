"""Text normalization library for comparing texts.

Provides three main functions:
    - normalize_numbers: Replace Polish number words with digits
    - normalize_text: Normalize text for comparison (lowercasing, diacritics, etc.)
    - normalize: Full normalization (numbers first, then text)
"""

from normalizacja_liczebnikow.normalizer import normalize_polish_numbers
from normalizacja_liczebnikow.diacritics import normalize_for_comparison


def normalize_numbers(text: str) -> str:
    """Replace Polish number words with digits in text.

    Args:
        text: Input text possibly containing Polish number words

    Returns:
        Text with Polish number words replaced by digits
    """
    return normalize_polish_numbers(text)


def normalize_text(text: str) -> str:
    """Normalize text for comparison purposes.

    Performs text-level normalization:
    - Removes Polish diacritics
    - Lowercases all characters
    - Removes punctuation except period, comma and question mark
    - Removes whitespace before retained punctuation
    - Deduplicates whitespace
    - Trims whitespace from beginning and end

    Args:
        text: Input text to normalize

    Returns:
        Normalized text suitable for comparison
    """
    return normalize_for_comparison(text)


def normalize(text: str) -> str:
    """Full normalization: numbers first, then text normalization.

    Applies number normalization (Polish number words → digits)
    followed by text normalization (lowercasing, diacritics removal, etc.).

    Args:
        text: Input text to fully normalize

    Returns:
        Fully normalized text
    """
    text = normalize_polish_numbers(text)
    return normalize_for_comparison(text)


__all__ = ['normalize_numbers', 'normalize_text', 'normalize']
