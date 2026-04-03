
import pytest
from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestInstrumental0to19:
    
    def test_zero_instrumental(self):
        assert normalize_polish_numbers("zerem") == "0"
    
    def test_one_instrumental(self):
        assert normalize_polish_numbers("jednym") == "1"
    
    def test_two_instrumental(self):
        assert normalize_polish_numbers("dwoma") == "2"
    
    def test_three_instrumental(self):
        assert normalize_polish_numbers("trzema") == "3"
    
    def test_four_instrumental(self):
        assert normalize_polish_numbers("czterema") == "4"
    
    def test_five_instrumental(self):
        assert normalize_polish_numbers("pięcioma") == "5"
    
    def test_six_instrumental(self):
        assert normalize_polish_numbers("sześcioma") == "6"
    
    def test_seven_instrumental(self):
        assert normalize_polish_numbers("siedmioma") == "7"
    
    def test_eight_instrumental(self):
        assert normalize_polish_numbers("ośmioma") == "8"
    
    def test_nine_instrumental(self):
        assert normalize_polish_numbers("dziewięcioma") == "9"
    
    def test_ten_instrumental(self):
        assert normalize_polish_numbers("dziesięcioma") == "10"
    
    def test_eleven_instrumental(self):
        assert normalize_polish_numbers("jedenastoma") == "11"
    
    def test_twelve_instrumental(self):
        assert normalize_polish_numbers("dwunastoma") == "12"
    
    def test_thirteen_instrumental(self):
        assert normalize_polish_numbers("trzynastoma") == "13"
    
    def test_fourteen_instrumental(self):
        assert normalize_polish_numbers("czternastoma") == "14"
    
    def test_fifteen_instrumental(self):
        assert normalize_polish_numbers("piętnastoma") == "15"
    
    def test_sixteen_instrumental(self):
        assert normalize_polish_numbers("szesnastoma") == "16"
    
    def test_seventeen_instrumental(self):
        assert normalize_polish_numbers("siedemnastoma") == "17"
    
    def test_eighteen_instrumental(self):
        assert normalize_polish_numbers("osiemnastoma") == "18"
    
    def test_nineteen_instrumental(self):
        assert normalize_polish_numbers("dziewiętnastoma") == "19"


class TestInstrumentalTens:
    
    def test_twenty_instrumental(self):
        assert normalize_polish_numbers("dwudziestoma") == "20"
    
    def test_thirty_instrumental(self):
        assert normalize_polish_numbers("trzydziestoma") == "30"
    
    def test_forty_instrumental(self):
        assert normalize_polish_numbers("czterdziestoma") == "40"
    
    def test_fifty_instrumental(self):
        assert normalize_polish_numbers("pięćdziesięcioma") == "50"
    
    def test_sixty_instrumental(self):
        assert normalize_polish_numbers("sześćdziesięcioma") == "60"
    
    def test_seventy_instrumental(self):
        assert normalize_polish_numbers("siedemdziesięcioma") == "70"
    
    def test_eighty_instrumental(self):
        assert normalize_polish_numbers("osiemdziesięcioma") == "80"
    
    def test_ninety_instrumental(self):
        assert normalize_polish_numbers("dziewięćdziesięcioma") == "90"


class TestInstrumentalHundreds:
    
    def test_one_hundred_instrumental(self):
        assert normalize_polish_numbers("stu") == "100"
    
    def test_two_hundred_instrumental(self):
        assert normalize_polish_numbers("dwustoma") == "200"
    
    def test_three_hundred_instrumental(self):
        assert normalize_polish_numbers("trzystoma") == "300"
    
    def test_four_hundred_instrumental(self):
        assert normalize_polish_numbers("czterystoma") == "400"
    
    def test_five_hundred_instrumental(self):
        assert normalize_polish_numbers("pięciuset") == "500"
    
    def test_six_hundred_instrumental(self):
        assert normalize_polish_numbers("sześciuset") == "600"
    
    def test_seven_hundred_instrumental(self):
        assert normalize_polish_numbers("siedmiuset") == "700"
    
    def test_eight_hundred_instrumental(self):
        assert normalize_polish_numbers("ośmiuset") == "800"
    
    def test_nine_hundred_instrumental(self):
        assert normalize_polish_numbers("dziewięciuset") == "900"


class TestInstrumentalThousands:
    
    def test_one_thousand_instrumental(self):
        assert normalize_polish_numbers("tysiącem") == "1000"
    
    def test_two_thousand_instrumental(self):
        assert normalize_polish_numbers("dwoma tysiącami") == "2000"
    
    def test_three_thousand_instrumental(self):
        assert normalize_polish_numbers("trzema tysiącami") == "3000"
    
    def test_four_thousand_instrumental(self):
        assert normalize_polish_numbers("czterema tysiącami") == "4000"
    
    def test_five_thousand_instrumental(self):
        assert normalize_polish_numbers("pięcioma tysiącami") == "5000"
    
    def test_six_thousand_instrumental(self):
        assert normalize_polish_numbers("sześcioma tysiącami") == "6000"
    
    def test_seven_thousand_instrumental(self):
        assert normalize_polish_numbers("siedmioma tysiącami") == "7000"
    
    def test_eight_thousand_instrumental(self):
        assert normalize_polish_numbers("ośmioma tysiącami") == "8000"
    
    def test_nine_thousand_instrumental(self):
        assert normalize_polish_numbers("dziewięcioma tysiącami") == "9000"


class TestInstrumentalCompoundNumbers:
    
    def test_twenty_one_instrumental(self):
        assert normalize_polish_numbers("dwudziestoma jeden") == "21"
    
    def test_twenty_five_instrumental(self):
        assert normalize_polish_numbers("dwudziestoma pięcioma") == "25"
    
    def test_hundred_one_instrumental(self):
        assert normalize_polish_numbers("sto jeden") == "101"
    
    def test_two_hundred_fifty_instrumental(self):
        assert normalize_polish_numbers("dwustoma pięćdziesięcioma") == "250"
    
    def test_one_thousand_one_instrumental(self):
        assert normalize_polish_numbers("tysiącem jeden") == "1001"
    
    def test_two_thousand_five_hundred_instrumental(self):
        assert normalize_polish_numbers("dwoma tysiącami pięciuset") == "2500"


class TestInstrumentalWithoutDiacritics:
    
    def test_two_instrumental_without_diacritics(self):
        assert normalize_polish_numbers("dwoma") == "2"
    
    def test_three_instrumental_without_diacritics(self):
        assert normalize_polish_numbers("trzema") == "3"
    
    def test_five_instrumental_without_diacritics(self):
        assert normalize_polish_numbers("pięcioma") == "5"
    
    def test_nine_instrumental_without_diacritics(self):
        assert normalize_polish_numbers("dziewięcioma") == "9"
    
    def test_one_hundred_instrumental_without_diacritics(self):
        assert normalize_polish_numbers("stu") == "100"
    
    def test_five_hundred_instrumental_without_diacritics(self):
        assert normalize_polish_numbers("pieciuset") == "500"
