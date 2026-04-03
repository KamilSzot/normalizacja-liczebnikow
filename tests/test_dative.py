
import pytest
from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestDativeDistinctForms:
    
    def test_one_dative(self):
        assert normalize_polish_numbers("jednemu") == "1"
    
    def test_two_dative(self):
        assert normalize_polish_numbers("dwóm") == "2"
        
    def test_two_dative2(self):
        assert normalize_polish_numbers("dwu") == "2"
    
    def test_three_dative(self):
        assert normalize_polish_numbers("trzem") == "3"
    
    def test_four_dative(self):
        assert normalize_polish_numbers("czterem") == "4"
    
    def test_one_thousand_dative(self):
        assert normalize_polish_numbers("tysiącowi") == "1000"
    
    def test_two_thousand_dative(self):
        assert normalize_polish_numbers("dwóm tysiącom") == "2000"
    
    def test_three_thousand_dative(self):
        assert normalize_polish_numbers("trzem tysiącom") == "3000"
    
    def test_four_thousand_dative(self):
        assert normalize_polish_numbers("czterem tysiącom") == "4000"
    
    def test_five_thousand_dative(self):
        assert normalize_polish_numbers("pięciu tysiącom") == "5000"
    
    def test_one_thousand_dative_without_diacritics(self):
        assert normalize_polish_numbers("tysiacowi") == "1000"


class TestDativeSharedWithGenitive:
    
    def test_five_dative(self):
        assert normalize_polish_numbers("pięciu") == "5"
    
    def test_ten_dative(self):
        assert normalize_polish_numbers("dziesięciu") == "10"
    
    def test_five_hundred_dative(self):
        assert normalize_polish_numbers("pięciuset") == "500"
