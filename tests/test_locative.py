
import pytest
from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestLocativeDistinctForms:

    def test_zero_locative(self):
        assert normalize_polish_numbers("zerze") == "0"

    def test_one_thousand_locative_singular(self):
        assert normalize_polish_numbers("tysiącu") == "1000"

    def test_one_thousand_locative_singular_without_diacritics(self):
        assert normalize_polish_numbers("tysiacu") == "1000"

    def test_two_thousand_locative_plural(self):
        assert normalize_polish_numbers("dwu tysiącach") == "2000"

    def test_two_thousand_locative_plural2(self):
        assert normalize_polish_numbers("dwóch tysiącach") == "2000"

    def test_three_thousand_locative_compound(self):
        assert normalize_polish_numbers("trzech tysiącach") == "3000"

    def test_four_thousand_locative_compound(self):
        assert normalize_polish_numbers("czterech tysiącach") == "4000"

    def test_five_thousand_locative_compound(self):
        assert normalize_polish_numbers("pięciu tysiącach") == "5000"

    def test_six_thousand_locative_compound(self):
        assert normalize_polish_numbers("sześciu tysiącach") == "6000"

    def test_seven_thousand_locative_compound(self):
        assert normalize_polish_numbers("siedmiu tysiącach") == "7000"

    def test_eight_thousand_locative_compound(self):
        assert normalize_polish_numbers("ośmiu tysiącach") == "8000"

    def test_nine_thousand_locative_compound(self):
        assert normalize_polish_numbers("dziewięciu tysiącach") == "9000"

    def test_ten_thousand_locative(self):
        assert (
            normalize_polish_numbers("dziesięciu tysiącach") == "10000"
        )  
