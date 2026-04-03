
import pytest
from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestNominativeFormsOnly:
    
    def test_zero_nominative(self):
        assert normalize_polish_numbers("zero") == "0"
    
    def test_one_nominative(self):
        assert normalize_polish_numbers("jeden") == "1"
    
    def test_two_nominative(self):
        assert normalize_polish_numbers("dwa") == "2"
    
    def test_three_nominative(self):
        assert normalize_polish_numbers("trzy") == "3"
    
    def test_four_nominative(self):
        assert normalize_polish_numbers("cztery") == "4"
    
    def test_five_nominative(self):
        assert normalize_polish_numbers("pięć") == "5"
    
    def test_six_nominative(self):
        assert normalize_polish_numbers("sześć") == "6"
    
    def test_seven_nominative(self):
        assert normalize_polish_numbers("siedem") == "7"
    
    def test_eight_nominative(self):
        assert normalize_polish_numbers("osiem") == "8"
    
    def test_nine_nominative(self):
        assert normalize_polish_numbers("dziewięć") == "9"
    
    def test_ten_nominative(self):
        assert normalize_polish_numbers("dziesięć") == "10"
    
    def test_eleven_nominative(self):
        assert normalize_polish_numbers("jedenaście") == "11"
    
    def test_twelve_nominative(self):
        assert normalize_polish_numbers("dwanaście") == "12"
    
    def test_thirteen_nominative(self):
        assert normalize_polish_numbers("trzynaście") == "13"
    
    def test_fourteen_nominative(self):
        assert normalize_polish_numbers("czternaście") == "14"
    
    def test_fifteen_nominative(self):
        assert normalize_polish_numbers("piętnaście") == "15"
    
    def test_sixteen_nominative(self):
        assert normalize_polish_numbers("szesnaście") == "16"
    
    def test_seventeen_nominative(self):
        assert normalize_polish_numbers("siedemnaście") == "17"
    
    def test_eighteen_nominative(self):
        assert normalize_polish_numbers("osiemnaście") == "18"
    
    def test_nineteen_nominative(self):
        assert normalize_polish_numbers("dziewiętnaście") == "19"
    
    def test_twenty_nominative(self):
        assert normalize_polish_numbers("dwadzieścia") == "20"
    
    def test_thirty_nominative(self):
        assert normalize_polish_numbers("trzydzieści") == "30"
    
    def test_forty_nominative(self):
        assert normalize_polish_numbers("czterdzieści") == "40"
    
    def test_fifty_nominative(self):
        assert normalize_polish_numbers("pięćdziesiąt") == "50"
    
    def test_sixty_nominative(self):
        assert normalize_polish_numbers("sześćdziesiąt") == "60"
    
    def test_seventy_nominative(self):
        assert normalize_polish_numbers("siedemdziesiąt") == "70"
    
    def test_eighty_nominative(self):
        assert normalize_polish_numbers("osiemdziesiąt") == "80"
    
    def test_ninety_nominative(self):
        assert normalize_polish_numbers("dziewięćdziesiąt") == "90"
    
    def test_one_hundred_nominative(self):
        assert normalize_polish_numbers("sto") == "100"
    
    def test_two_hundred_nominative(self):
        assert normalize_polish_numbers("dwieście") == "200"
    
    def test_three_hundred_nominative(self):
        assert normalize_polish_numbers("trzysta") == "300"
    
    def test_four_hundred_nominative(self):
        assert normalize_polish_numbers("czterysta") == "400"
    
    def test_five_hundred_nominative(self):
        assert normalize_polish_numbers("pięćset") == "500"
    
    def test_six_hundred_nominative(self):
        assert normalize_polish_numbers("sześćset") == "600"
    
    def test_seven_hundred_nominative(self):
        assert normalize_polish_numbers("siedemset") == "700"
    
    def test_eight_hundred_nominative(self):
        assert normalize_polish_numbers("osiemset") == "800"
    
    def test_nine_hundred_nominative(self):
        assert normalize_polish_numbers("dziewięćset") == "900"
    
    def test_one_thousand_nominative(self):
        assert normalize_polish_numbers("tysiąc") == "1000"
    
    def test_two_thousand_nominative(self):
        assert normalize_polish_numbers("dwa tysiące") == "2000"
    
    def test_three_thousand_nominative(self):
        assert normalize_polish_numbers("trzy tysiące") == "3000"
    
    def test_four_thousand_nominative(self):
        assert normalize_polish_numbers("cztery tysiące") == "4000"
    
    def test_five_thousand_nominative(self):
        assert normalize_polish_numbers("pięć tysięcy") == "5000"
    
    def test_six_thousand_nominative(self):
        assert normalize_polish_numbers("sześć tysięcy") == "6000"
    
    def test_seven_thousand_nominative(self):
        assert normalize_polish_numbers("siedem tysięcy") == "7000"
    
    def test_eight_thousand_nominative(self):
        assert normalize_polish_numbers("osiem tysięcy") == "8000"
    
    def test_nine_thousand_nominative(self):
        assert normalize_polish_numbers("dziewięć tysięcy") == "9000"
    
    def test_ten_thousand_nominative(self):
        assert normalize_polish_numbers("dziesięć tysięcy") == "10000"
    
    def test_twenty_thousand_nominative(self):
        assert normalize_polish_numbers("dwadzieścia tysięcy") == "20000"
    
    def test_thirty_thousand_nominative(self):
        assert normalize_polish_numbers("trzydzieści tysięcy") == "30000"
    
    def test_forty_thousand_nominative(self):
        assert normalize_polish_numbers("czterdzieści tysięcy") == "40000"
    
    def test_fifty_thousand_nominative(self):
        assert normalize_polish_numbers("pięćdziesiąt tysięcy") == "50000"
    
    def test_sixty_thousand_nominative(self):
        assert normalize_polish_numbers("sześćdziesiąt tysięcy") == "60000"
    
    def test_seventy_thousand_nominative(self):
        assert normalize_polish_numbers("siedemdziesiąt tysięcy") == "70000"
    
    def test_eighty_thousand_nominative(self):
        assert normalize_polish_numbers("osiemdziesiąt tysięcy") == "80000"
    
    def test_ninety_thousand_nominative(self):
        assert normalize_polish_numbers("dziewięćdziesiąt tysięcy") == "90000"
