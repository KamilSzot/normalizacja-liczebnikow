
import pytest
from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestAccusative0to19:
    
    def test_zero_accusative(self):
        assert normalize_polish_numbers("zero") == "0"
    
    def test_one_accusative(self):
        assert normalize_polish_numbers("jednego") == "1"
    
    def test_two_accusative(self):
        assert normalize_polish_numbers("dwa") == "2"
    
    def test_three_accusative(self):
        assert normalize_polish_numbers("trzy") == "3"
    
    def test_four_accusative(self):
        assert normalize_polish_numbers("cztery") == "4"
    
    def test_five_accusative(self):
        assert normalize_polish_numbers("pięć") == "5"
    
    def test_six_accusative(self):
        assert normalize_polish_numbers("sześć") == "6"
    
    def test_seven_accusative(self):
        assert normalize_polish_numbers("siedem") == "7"
    
    def test_eight_accusative(self):
        assert normalize_polish_numbers("osiem") == "8"
    
    def test_nine_accusative(self):
        assert normalize_polish_numbers("dziewięć") == "9"
    
    def test_ten_accusative(self):
        assert normalize_polish_numbers("dziesięć") == "10"
    
    def test_eleven_accusative(self):
        assert normalize_polish_numbers("jedenaście") == "11"
    
    def test_twelve_accusative(self):
        assert normalize_polish_numbers("dwanaście") == "12"
    
    def test_thirteen_accusative(self):
        assert normalize_polish_numbers("trzynaście") == "13"
    
    def test_fourteen_accusative(self):
        assert normalize_polish_numbers("czternaście") == "14"
    
    def test_fifteen_accusative(self):
        assert normalize_polish_numbers("piętnaście") == "15"
    
    def test_sixteen_accusative(self):
        assert normalize_polish_numbers("szesnaście") == "16"
    
    def test_seventeen_accusative(self):
        assert normalize_polish_numbers("siedemnaście") == "17"
    
    def test_eighteen_accusative(self):
        assert normalize_polish_numbers("osiemnaście") == "18"
    
    def test_nineteen_accusative(self):
        assert normalize_polish_numbers("dziewiętnaście") == "19"


class TestAccusativeTens:
    
    def test_twenty_accusative(self):
        assert normalize_polish_numbers("dwadzieścia") == "20"
    
    def test_thirty_accusative(self):
        assert normalize_polish_numbers("trzydzieści") == "30"
    
    def test_forty_accusative(self):
        assert normalize_polish_numbers("czterdzieści") == "40"
    
    def test_fifty_accusative(self):
        assert normalize_polish_numbers("pięćdziesiąt") == "50"
    
    def test_sixty_accusative(self):
        assert normalize_polish_numbers("sześćdziesiąt") == "60"
    
    def test_seventy_accusative(self):
        assert normalize_polish_numbers("siedemdziesiąt") == "70"
    
    def test_eighty_accusative(self):
        assert normalize_polish_numbers("osiemdziesiąt") == "80"
    
    def test_ninety_accusative(self):
        assert normalize_polish_numbers("dziewięćdziesiąt") == "90"


class TestAccusativeHundreds:
    
    def test_one_hundred_accusative(self):
        assert normalize_polish_numbers("sto") == "100"
    
    def test_two_hundred_accusative(self):
        assert normalize_polish_numbers("dwieście") == "200"
    
    def test_three_hundred_accusative(self):
        assert normalize_polish_numbers("trzysta") == "300"
    
    def test_four_hundred_accusative(self):
        assert normalize_polish_numbers("czterysta") == "400"
    
    def test_five_hundred_accusative(self):
        assert normalize_polish_numbers("pięćset") == "500"
    
    def test_six_hundred_accusative(self):
        assert normalize_polish_numbers("sześćset") == "600"
    
    def test_seven_hundred_accusative(self):
        assert normalize_polish_numbers("siedemset") == "700"
    
    def test_eight_hundred_accusative(self):
        assert normalize_polish_numbers("osiemset") == "800"
    
    def test_nine_hundred_accusative(self):
        assert normalize_polish_numbers("dziewięćset") == "900"


class TestAccusativeThousands:
    
    def test_one_thousand_accusative(self):
        assert normalize_polish_numbers("tysiąc") == "1000"
    
    def test_two_thousand_accusative(self):
        assert normalize_polish_numbers("dwa tysiące") == "2000"
    
    def test_three_thousand_accusative(self):
        assert normalize_polish_numbers("trzy tysiące") == "3000"
    
    def test_four_thousand_accusative(self):
        assert normalize_polish_numbers("cztery tysiące") == "4000"
    
    def test_five_thousand_accusative(self):
        assert normalize_polish_numbers("pięć tysięcy") == "5000"
    
    def test_six_thousand_accusative(self):
        assert normalize_polish_numbers("sześć tysięcy") == "6000"
    
    def test_seven_thousand_accusative(self):
        assert normalize_polish_numbers("siedem tysięcy") == "7000"
    
    def test_eight_thousand_accusative(self):
        assert normalize_polish_numbers("osiem tysięcy") == "8000"
    
    def test_nine_thousand_accusative(self):
        assert normalize_polish_numbers("dziewięć tysięcy") == "9000"


class TestAccusativeCompoundNumbers:
    
    def test_twenty_one_accusative(self):
        assert normalize_polish_numbers("dwadzieścia jeden") == "21"
    
    def test_twenty_five_accusative(self):
        assert normalize_polish_numbers("dwadzieścia pięć") == "25"
    
    def test_hundred_one_accusative(self):
        assert normalize_polish_numbers("sto jeden") == "101"
    
    def test_two_hundred_fifty_accusative(self):
        assert normalize_polish_numbers("dwieście pięćdziesiąt") == "250"
    
    def test_one_thousand_one_accusative(self):
        assert normalize_polish_numbers("tysiąc jeden") == "1001"
    
    def test_two_thousand_five_hundred_accusative(self):
        assert normalize_polish_numbers("dwa tysiące pięćset") == "2500"


class TestAccusativeWithoutDiacritics:
    
    def test_two_accusative_without_diacritics(self):
        assert normalize_polish_numbers("dwa") == "2"
    
    def test_three_accusative_without_diacritics(self):
        assert normalize_polish_numbers("trzy") == "3"
    
    def test_five_accusative_without_diacritics(self):
        assert normalize_polish_numbers("piec") == "5"
    
    def test_nine_accusative_without_diacritics(self):
        assert normalize_polish_numbers("dziewiec") == "9"
    
    def test_one_hundred_accusative_without_diacritics(self):
        assert normalize_polish_numbers("sto") == "100"
    
    def test_five_hundred_accusative_without_diacritics(self):
        assert normalize_polish_numbers("piecset") == "500"
