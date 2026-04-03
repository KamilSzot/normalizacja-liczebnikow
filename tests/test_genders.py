
import pytest
from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestOneGenderVariants:
    
    def test_jeden_masculine_nominative(self):
        assert normalize_polish_numbers("jeden") == "1"
    
    def test_jedna_feminine_nominative(self):
        assert normalize_polish_numbers("jedna") == "1"
    
    def test_jedno_neuter_nominative(self):
        assert normalize_polish_numbers("jedno") == "1"
    
    def test_jednego_masculine_neuter_genitive(self):
        assert normalize_polish_numbers("jednego") == "1"
    
    def test_jednemu_masculine_neuter_dative(self):
        assert normalize_polish_numbers("jednemu") == "1"
    
    def test_jednego_masculine_accusative(self):
        assert normalize_polish_numbers("jednego") == "1"
    
    def test_jedną_feminine_accusative(self):
        assert normalize_polish_numbers("jedną") == "1"
    
    def test_jednym_masculine_neuter_instrumental(self):
        assert normalize_polish_numbers("jednym") == "1"
    
    def test_jedną_feminine_instrumental(self):
        assert normalize_polish_numbers("jedną") == "1"


class TestTwoGenderVariants:
    
    def test_dwa_masculine_nonpersonal_nominative(self):
        assert normalize_polish_numbers("dwa") == "2"
    
    def test_dwaj_masculine_personal_nominative(self):
        assert normalize_polish_numbers("dwaj") == "2"
    
    def test_dwie_feminine_nominative(self):
        assert normalize_polish_numbers("dwie") == "2"
    
    def test_dwóch_masculine_personal_genitive(self):
        assert normalize_polish_numbers("dwóch") == "2"
    
    def test_dwóm_masculine_dative(self):
        assert normalize_polish_numbers("dwóm") == "2"
    
    def test_dwu_masculine_personal_dative(self):
        assert normalize_polish_numbers("dwu") == "2"
    
    def test_dwóch_masculine_personal_accusative(self):
        assert normalize_polish_numbers("dwóch") == "2"
    
    def test_dwoma_masculine_instrumental(self):
        assert normalize_polish_numbers("dwoma") == "2"


class TestThreeGenderVariants:
    
    def test_trzy_feminine_neuter_nominative(self):
        assert normalize_polish_numbers("trzy") == "3"
    
    def test_trzej_masculine_personal_nominative(self):
        assert normalize_polish_numbers("trzej") == "3"
    
    def test_trzech_masculine_personal_genitive(self):
        assert normalize_polish_numbers("trzech") == "3"
    
    def test_trzem_masculine_dative(self):
        assert normalize_polish_numbers("trzem") == "3"
    
    def test_trzech_masculine_personal_accusative(self):
        assert normalize_polish_numbers("trzech") == "3"
    
    def test_trzema_masculine_instrumental(self):
        assert normalize_polish_numbers("trzema") == "3"


class TestFourGenderVariants:
    
    def test_cztery_feminine_neuter_nominative(self):
        assert normalize_polish_numbers("cztery") == "4"
    
    def test_czterej_masculine_personal_nominative(self):
        assert normalize_polish_numbers("czterej") == "4"
    
    def test_czterech_masculine_personal_genitive(self):
        assert normalize_polish_numbers("czterech") == "4"
    
    def test_czterem_masculine_dative(self):
        assert normalize_polish_numbers("czterem") == "4"
    
    def test_czterech_masculine_personal_accusative(self):
        assert normalize_polish_numbers("czterech") == "4"
    
    def test_czterema_masculine_instrumental(self):
        assert normalize_polish_numbers("czterema") == "4"
