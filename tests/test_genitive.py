
import pytest
from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestGenitive0to19:
    
    def test_zero_genitive(self):
        assert normalize_polish_numbers("zera") == "0"
    
    def test_one_genitive(self):
        assert normalize_polish_numbers("jednego") == "1"
    
    def test_two_genitive(self):
        assert normalize_polish_numbers("dwóch") == "2"
    
    def test_three_genitive(self):
        assert normalize_polish_numbers("trzech") == "3"
    
    def test_four_genitive(self):
        assert normalize_polish_numbers("czterech") == "4"
    
    def test_five_genitive(self):
        assert normalize_polish_numbers("pięciu") == "5"
    
    def test_six_genitive(self):
        assert normalize_polish_numbers("sześciu") == "6"
    
    def test_seven_genitive(self):
        assert normalize_polish_numbers("siedmiu") == "7"
    
    def test_eight_genitive(self):
        assert normalize_polish_numbers("ośmiu") == "8"
    
    def test_nine_genitive(self):
        assert normalize_polish_numbers("dziewięciu") == "9"
    
    def test_ten_genitive(self):
        assert normalize_polish_numbers("dziesięciu") == "10"
    
    def test_eleven_genitive(self):
        assert normalize_polish_numbers("jedenastu") == "11"
    
    def test_twelve_genitive(self):
        assert normalize_polish_numbers("dwunastu") == "12"
    
    def test_thirteen_genitive(self):
        assert normalize_polish_numbers("trzynastu") == "13"
    
    def test_fourteen_genitive(self):
        assert normalize_polish_numbers("czternastu") == "14"
    
    def test_fifteen_genitive(self):
        assert normalize_polish_numbers("piętnastu") == "15"
    
    def test_sixteen_genitive(self):
        assert normalize_polish_numbers("szesnastu") == "16"
    
    def test_seventeen_genitive(self):
        assert normalize_polish_numbers("siedemnastu") == "17"
    
    def test_eighteen_genitive(self):
        assert normalize_polish_numbers("osiemnastu") == "18"
    
    def test_nineteen_genitive(self):
        assert normalize_polish_numbers("dziewiętnastu") == "19"


class TestGenitiveTens:
    
    def test_twenty_genitive(self):
        assert normalize_polish_numbers("dwudziestu") == "20"
    
    def test_thirty_genitive(self):
        assert normalize_polish_numbers("trzydziestu") == "30"
    
    def test_forty_genitive(self):
        assert normalize_polish_numbers("czterdziestu") == "40"
    
    def test_fifty_genitive(self):
        assert normalize_polish_numbers("pięćdziesięciu") == "50"
    
    def test_sixty_genitive(self):
        assert normalize_polish_numbers("sześćdziesięciu") == "60"
    
    def test_seventy_genitive(self):
        assert normalize_polish_numbers("siedemdziesięciu") == "70"
    
    def test_eighty_genitive(self):
        assert normalize_polish_numbers("osiemdziesięciu") == "80"
    
    def test_ninety_genitive(self):
        assert normalize_polish_numbers("dziewięćdziesięciu") == "90"


class TestGenitiveHundreds:
    
    def test_one_hundred_genitive(self):
        assert normalize_polish_numbers("stu") == "100"
    
    def test_two_hundred_genitive(self):
        assert normalize_polish_numbers("dwustu") == "200"
    
    def test_three_hundred_genitive(self):
        assert normalize_polish_numbers("trzystu") == "300"
    
    def test_four_hundred_genitive(self):
        assert normalize_polish_numbers("czterystu") == "400"
    
    def test_five_hundred_genitive(self):
        assert normalize_polish_numbers("pięciuset") == "500"
    
    def test_six_hundred_genitive(self):
        assert normalize_polish_numbers("sześciuset") == "600"
    
    def test_seven_hundred_genitive(self):
        assert normalize_polish_numbers("siedmiuset") == "700"
    
    def test_eight_hundred_genitive(self):
        assert normalize_polish_numbers("ośmiuset") == "800"
    
    def test_nine_hundred_genitive(self):
        assert normalize_polish_numbers("dziewięciuset") == "900"


class TestGenitiveThousands:
    
    def test_one_thousand_genitive(self):
        assert normalize_polish_numbers("tysiąca") == "1000"
    
    def test_two_thousand_genitive(self):
        assert normalize_polish_numbers("dwóch tysięcy") == "2000"
    
    def test_three_thousand_genitive(self):
        assert normalize_polish_numbers("trzech tysięcy") == "3000"
    
    def test_four_thousand_genitive(self):
        assert normalize_polish_numbers("czterech tysięcy") == "4000"
    
    def test_five_thousand_genitive(self):
        assert normalize_polish_numbers("pięciu tysięcy") == "5000"
    
    def test_six_thousand_genitive(self):
        assert normalize_polish_numbers("sześciu tysięcy") == "6000"
    
    def test_seven_thousand_genitive(self):
        assert normalize_polish_numbers("siedmiu tysięcy") == "7000"
    
    def test_eight_thousand_genitive(self):
        assert normalize_polish_numbers("ośmiu tysięcy") == "8000"
    
    def test_nine_thousand_genitive(self):
        assert normalize_polish_numbers("dziewięciu tysięcy") == "9000"


class TestGenitiveCompoundNumbers:
    
    def test_twenty_one_genitive(self):
        assert normalize_polish_numbers("dwudziestu jeden") == "21"
    
    def test_twenty_five_genitive(self):
        assert normalize_polish_numbers("dwudziestu pięciu") == "25"
    
    def test_hundred_one_genitive(self):
        assert normalize_polish_numbers("stu jeden") == "101"
    
    def test_two_hundred_fifty_genitive(self):
        assert normalize_polish_numbers("dwustu pięćdziesięciu") == "250"
    
    def test_one_thousand_one_genitive(self):
        assert normalize_polish_numbers("tysiąca jeden") == "1001"
    
    def test_two_thousand_five_hundred_genitive(self):
        assert normalize_polish_numbers("dwóch tysięcy pięciuset") == "2500"


class TestGenitiveWithoutDiacritics:
    
    def test_two_genitive_without_diacritics(self):
        assert normalize_polish_numbers("dwoch") == "2"
    
    def test_three_genitive_without_diacritics(self):
        assert normalize_polish_numbers("trzech") == "3"
    
    def test_five_genitive_without_diacritics(self):
        assert normalize_polish_numbers("pieciu") == "5"
    
    def test_nine_genitive_without_diacritics(self):
        assert normalize_polish_numbers("dziewieciu") == "9"
    
    def test_one_hundred_genitive_without_diacritics(self):
        assert normalize_polish_numbers("stu") == "100"
    
    def test_five_hundred_genitive_without_diacritics(self):
        assert normalize_polish_numbers("pieciuset") == "500"
