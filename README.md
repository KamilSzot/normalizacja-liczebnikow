# normalizacja-liczebnikow

A text normalization library for comparing Polish texts. It replaces Polish number words with digits and normalizes text for comparison purposes.

## Installation

Build the package:

```bash
# Windows
./build.ps1

# Linux/macOS
./build.sh
```

Install in another project:

```bash
pip install dist/normalizacja_liczebnikow-0.1.0-py3-none-any.whl
```

## API

Three functions are exposed:

### `normalize_numbers(text)`

Replaces Polish number words with digits. Handles cardinals, ordinals, compound numbers, and all inflected forms across grammatical cases.

```python
from src import normalize_numbers

normalize_numbers("Mam pięćset dwadzieścia trzy jabłka")
# → "Mam 523 jabłka"

normalize_numbers("To jest dwudziesty piąty rozdział")
# → "To jest 25 rozdział"

normalize_numbers("Przejechaliśmy dwadzieścia pięć tysięcy kilometrów")
# → "Przejechaliśmy 25000 kilometrów"
```

### `normalize_text(text)`

Normalizes text for comparison. Removes Polish diacritics, lowercases, strips punctuation (except period, comma, and question mark), removes whitespace before retained punctuation, deduplicates whitespace, trims, and strips leading/trailing punctuation (periods and commas from both ends, question marks from the beginning only).

```python
from src import normalize_text

normalize_text("Mam 523 jabłka, dwadzieścia gruszek i 12 śliwek.")
# → "mam 523 jablka, dwadziescia gruszek i 12 sliwek"

normalize_text("Czy masz 25 złotych?")
# → "czy masz 25 zlotych?"
```

### `normalize(text)`

Full normalization pipeline: applies number normalization first, then text normalization.

```python
from src import normalize

normalize("Mam pięćset dwadzieścia trzy jabłka, dwadzieścia gruszek i dwanaście śliwek.")
# → "mam 523 jablka, 20 gruszek i 12 sliwek"

normalize("Czy masz dwadzieścia pięć złotych?")
# → "czy masz 25 zlotych?"
```

## What's Supported

### Number Types

- **Cardinals** — 0 through 99,999 in all inflected forms (nominative, genitive, dative, accusative, instrumental, locative)
- **Ordinals** — 1st through 90,000th in masculine, feminine, and neuter genders, plus declined forms
- **Compound numbers** — multi-word combinations like `pięćset dwadzieścia trzy` → 523
- **Thousands** — with grammatical agreement: `dwa tysiące` → 2000, `pięć tysięcy` → 5000
- **Mixed text** — numbers embedded in running text alongside non-number words
- **Case insensitivity** — `PIĘĆ`, `Pięć`, `pięć` all resolve to 5
- **Diacritic insensitivity** — `pięć` and `piec` both resolve to 5

### Text Normalization

- Polish diacritic removal (ą→a, ć→c, ę→e, ł→l, ń→n, ó→o, ś→s, ź→z, ż→z)
- Lowercasing
- Punctuation removal with selective preservation of `.`, `,`, `?`
- Whitespace before retained punctuation is collapsed (`"hello , world"` → `"hello, world"`)
- Whitespace deduplication and trimming
- Leading/trailing punctuation stripping (`.`, `,` from both ends; `?` from beginning only)

## Limitations

### Numbers beyond 99,999

The parser handles numbers up to 99,999 (e.g. `dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć` → 99,999). Numbers of 100,000 and above are not supported.

### Fractional expressions

Expressions with fractional components are not composed into a single quantity:

```python
normalize_numbers("dwa i pół tysiąca")
# → "2 i pół 1000" (expected: "2500")

normalize_numbers("półtora tysiąca")
# → "półtora 1000" (expected: "1500")
```

### Range ellipsis

Range-like expressions where a shared noun should apply to both numbers are interpreted literally:

```python
normalize_numbers("od pięciu do siedmiu tysięcy")
# → "od 5 do 7 1000" (expected: "od 5000 do 7000")
```

### Elliptic coordination

When a compound number is followed by a disjunction, the composed prefix is not propagated to the second conjunct:

```python
normalize_numbers("dwieście trzy lub cztery osoby")
# → "203 lub 4 osoby" (expected: "203 lub 204 osoby")
```

### Abbreviated year coordination

Year phrases with an elided shared prefix are not reconstructed:

```python
normalize_numbers("w latach tysiąc dziewięćset osiemdziesiąty dziewiąty i dziewięćdziesiąty")
# → "w latach 1989 i 90" (expected: "w latach 1989 i 1990")
```

### Hyphenated compounds

Words connected by hyphens are not grouped into a single compound. Each segment is parsed independently:

```python
normalize_numbers("dwadzieścia-trzy")
# → "20-3" (not "23")
```

### No million/billion support

Words like `milion`, `miliard` are not recognized.

## Development

Requires [uv](https://docs.astral.sh/uv/) and Python 3.13+.

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest tests/ -v

# Build package
./build.ps1    # Windows
./build.sh     # Linux/macOS
```

## Technical Documentation

For a detailed description of how the modules work internally, see [plans/how-it-works.md](plans/how-it-works.md).
