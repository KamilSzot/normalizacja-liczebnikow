
import pytest
from src.normalizer import normalize_polish_numbers


class TestCardinalNumbers0to19:
    
    def test_zero(self):
        assert normalize_polish_numbers("zero") == "0"
        assert normalize_polish_numbers("zera") == "0"
        assert normalize_polish_numbers("zerem") == "0"
        assert normalize_polish_numbers("zerze") == "0"
    
    def test_one(self):
        assert normalize_polish_numbers("jeden") == "1"
        assert normalize_polish_numbers("jednego") == "1"
        assert normalize_polish_numbers("jednym") == "1"
    
    def test_two(self):
        assert normalize_polish_numbers("dwa") == "2"
        assert normalize_polish_numbers("dwóch") == "2"
        assert normalize_polish_numbers("dwoma") == "2"
    
    def test_three(self):
        assert normalize_polish_numbers("trzy") == "3"
        assert normalize_polish_numbers("trzech") == "3"
        assert normalize_polish_numbers("trzema") == "3"
    
    def test_four(self):
        assert normalize_polish_numbers("cztery") == "4"
        assert normalize_polish_numbers("czterech") == "4"
        assert normalize_polish_numbers("czterema") == "4"
    
    def test_five(self):
        assert normalize_polish_numbers("pięć") == "5"
        assert normalize_polish_numbers("pięciu") == "5"
        assert normalize_polish_numbers("pięcioma") == "5"
    
    def test_six(self):
        assert normalize_polish_numbers("sześć") == "6"
        assert normalize_polish_numbers("sześciu") == "6"
        assert normalize_polish_numbers("sześcioma") == "6"
    
    def test_seven(self):
        assert normalize_polish_numbers("siedem") == "7"
        assert normalize_polish_numbers("siedmiu") == "7"
        assert normalize_polish_numbers("siedmioma") == "7"
    
    def test_eight(self):
        assert normalize_polish_numbers("osiem") == "8"
        assert normalize_polish_numbers("ośmiu") == "8"
        assert normalize_polish_numbers("ośmioma") == "8"
    
    def test_nine(self):
        assert normalize_polish_numbers("dziewięć") == "9"
        assert normalize_polish_numbers("dziewięciu") == "9"
        assert normalize_polish_numbers("dziewięcioma") == "9"
    
    def test_ten(self):
        assert normalize_polish_numbers("dziesięć") == "10"
        assert normalize_polish_numbers("dziesięciu") == "10"
        assert normalize_polish_numbers("dziesięcioma") == "10"
    
    def test_eleven(self):
        assert normalize_polish_numbers("jedenaście") == "11"
        assert normalize_polish_numbers("jedenastu") == "11"
        assert normalize_polish_numbers("jedenastoma") == "11"
    
    def test_twelve(self):
        assert normalize_polish_numbers("dwanaście") == "12"
        assert normalize_polish_numbers("dwunastu") == "12"
        assert normalize_polish_numbers("dwunastoma") == "12"
    
    def test_thirteen(self):
        assert normalize_polish_numbers("trzynaście") == "13"
        assert normalize_polish_numbers("trzynastu") == "13"
        assert normalize_polish_numbers("trzynastoma") == "13"
    
    def test_fourteen(self):
        assert normalize_polish_numbers("czternaście") == "14"
        assert normalize_polish_numbers("czternastu") == "14"
        assert normalize_polish_numbers("czternastoma") == "14"
    
    def test_fifteen(self):
        assert normalize_polish_numbers("piętnaście") == "15"
        assert normalize_polish_numbers("piętnastu") == "15"
        assert normalize_polish_numbers("piętnastoma") == "15"
    
    def test_sixteen(self):
        assert normalize_polish_numbers("szesnaście") == "16"
        assert normalize_polish_numbers("szesnastu") == "16"
        assert normalize_polish_numbers("szesnastoma") == "16"
    
    def test_seventeen(self):
        assert normalize_polish_numbers("siedemnaście") == "17"
        assert normalize_polish_numbers("siedemnastu") == "17"
        assert normalize_polish_numbers("siedemnastoma") == "17"
    
    def test_eighteen(self):
        assert normalize_polish_numbers("osiemnaście") == "18"
        assert normalize_polish_numbers("osiemnastu") == "18"
        assert normalize_polish_numbers("osiemnastoma") == "18"
    
    def test_nineteen(self):
        assert normalize_polish_numbers("dziewiętnaście") == "19"
        assert normalize_polish_numbers("dziewiętnastu") == "19"
        assert normalize_polish_numbers("dziewiętnastoma") == "19"


class TestCardinalNumbersTens:
    
    def test_twenty(self):
        assert normalize_polish_numbers("dwadzieścia") == "20"
        assert normalize_polish_numbers("dwudziestu") == "20"
        assert normalize_polish_numbers("dwudziestoma") == "20"
    
    def test_thirty(self):
        assert normalize_polish_numbers("trzydzieści") == "30"
        assert normalize_polish_numbers("trzydziestu") == "30"
        assert normalize_polish_numbers("trzydziestoma") == "30"
    
    def test_forty(self):
        assert normalize_polish_numbers("czterdzieści") == "40"
        assert normalize_polish_numbers("czterdziestu") == "40"
        assert normalize_polish_numbers("czterdziestoma") == "40"
    
    def test_fifty(self):
        assert normalize_polish_numbers("pięćdziesiąt") == "50"
        assert normalize_polish_numbers("pięćdziesięciu") == "50"
        assert normalize_polish_numbers("pięćdziesięcioma") == "50"
    
    def test_sixty(self):
        assert normalize_polish_numbers("sześćdziesiąt") == "60"
        assert normalize_polish_numbers("sześćdziesięciu") == "60"
        assert normalize_polish_numbers("sześćdziesięcioma") == "60"
    
    def test_seventy(self):
        assert normalize_polish_numbers("siedemdziesiąt") == "70"
        assert normalize_polish_numbers("siedemdziesięciu") == "70"
        assert normalize_polish_numbers("siedemdziesięcioma") == "70"
    
    def test_eighty(self):
        assert normalize_polish_numbers("osiemdziesiąt") == "80"
        assert normalize_polish_numbers("osiemdziesięciu") == "80"
        assert normalize_polish_numbers("osiemdziesięcioma") == "80"
    
    def test_ninety(self):
        assert normalize_polish_numbers("dziewięćdziesiąt") == "90"
        assert normalize_polish_numbers("dziewięćdziesięciu") == "90"
        assert normalize_polish_numbers("dziewięćdziesięcioma") == "90"


class TestCardinalNumbersHundreds:
    
    def test_one_hundred(self):
        assert normalize_polish_numbers("sto") == "100"
        assert normalize_polish_numbers("stu") == "100"
    
    def test_two_hundred(self):
        assert normalize_polish_numbers("dwieście") == "200"
        assert normalize_polish_numbers("dwustu") == "200"
        assert normalize_polish_numbers("dwustoma") == "200"
    
    def test_three_hundred(self):
        assert normalize_polish_numbers("trzysta") == "300"
        assert normalize_polish_numbers("trzystu") == "300"
        assert normalize_polish_numbers("trzystoma") == "300"
    
    def test_four_hundred(self):
        assert normalize_polish_numbers("czterysta") == "400"
        assert normalize_polish_numbers("czterystu") == "400"
        assert normalize_polish_numbers("czterystoma") == "400"
    
    def test_five_hundred(self):
        assert normalize_polish_numbers("pięćset") == "500"
        assert normalize_polish_numbers("pięciuset") == "500"
    
    def test_six_hundred(self):
        assert normalize_polish_numbers("sześćset") == "600"
        assert normalize_polish_numbers("sześciuset") == "600"
    
    def test_seven_hundred(self):
        assert normalize_polish_numbers("siedemset") == "700"
        assert normalize_polish_numbers("siedmiuset") == "700"
    
    def test_eight_hundred(self):
        assert normalize_polish_numbers("osiemset") == "800"
        assert normalize_polish_numbers("ośmiuset") == "800"
    
    def test_nine_hundred(self):
        assert normalize_polish_numbers("dziewięćset") == "900"
        assert normalize_polish_numbers("dziewięciuset") == "900"


class TestCardinalNumbersThousands:
    
    def test_one_thousand(self):
        assert normalize_polish_numbers("tysiąc") == "1000"
        assert normalize_polish_numbers("tysiąca") == "1000"
        assert normalize_polish_numbers("tysiącem") == "1000"
        assert normalize_polish_numbers("tysiącu") == "1000"
    
    def test_two_thousand(self):
        assert normalize_polish_numbers("dwa tysiące") == "2000"
        assert normalize_polish_numbers("dwóch tysięcy") == "2000"
        assert normalize_polish_numbers("dwoma tysiącami") == "2000"
    
    def test_three_thousand(self):
        assert normalize_polish_numbers("trzy tysiące") == "3000"
        assert normalize_polish_numbers("trzech tysięcy") == "3000"
        assert normalize_polish_numbers("trzema tysiącami") == "3000"
    
    def test_four_thousand(self):
        assert normalize_polish_numbers("cztery tysiące") == "4000"
        assert normalize_polish_numbers("czterech tysięcy") == "4000"
        assert normalize_polish_numbers("czterema tysiącami") == "4000"
    
    def test_five_thousand(self):
        assert normalize_polish_numbers("pięć tysięcy") == "5000"
        assert normalize_polish_numbers("pięciu tysięcy") == "5000"
        assert normalize_polish_numbers("pięcioma tysiącami") == "5000"
    
    def test_six_thousand(self):
        assert normalize_polish_numbers("sześć tysięcy") == "6000"
        assert normalize_polish_numbers("sześciu tysięcy") == "6000"
        assert normalize_polish_numbers("sześcioma tysiącami") == "6000"
    
    def test_seven_thousand(self):
        assert normalize_polish_numbers("siedem tysięcy") == "7000"
        assert normalize_polish_numbers("siedmiu tysięcy") == "7000"
        assert normalize_polish_numbers("siedmioma tysiącami") == "7000"
    
    def test_eight_thousand(self):
        assert normalize_polish_numbers("osiem tysięcy") == "8000"
        assert normalize_polish_numbers("ośmiu tysięcy") == "8000"
        assert normalize_polish_numbers("ośmioma tysiącami") == "8000"
    
    def test_nine_thousand(self):
        assert normalize_polish_numbers("dziewięć tysięcy") == "9000"
        assert normalize_polish_numbers("dziewięciu tysięcy") == "9000"
        assert normalize_polish_numbers("dziewięcioma tysiącami") == "9000"


class TestCardinalNumbersTenThousands:
    
    def test_ten_thousand(self):
        assert normalize_polish_numbers("dziesięć tysięcy") == "10000"
        assert normalize_polish_numbers("dziesięciu tysięcy") == "10000"
        assert normalize_polish_numbers("dziesięcioma tysiącami") == "10000"
    
    def test_twenty_thousand(self):
        assert normalize_polish_numbers("dwadzieścia tysięcy") == "20000"
        assert normalize_polish_numbers("dwudziestu tysięcy") == "20000"
        assert normalize_polish_numbers("dwudziestoma tysiącami") == "20000"
    
    def test_thirty_thousand(self):
        assert normalize_polish_numbers("trzydzieści tysięcy") == "30000"
        assert normalize_polish_numbers("trzydziestu tysięcy") == "30000"
        assert normalize_polish_numbers("trzydziestoma tysiącami") == "30000"
    
    def test_forty_thousand(self):
        assert normalize_polish_numbers("czterdzieści tysięcy") == "40000"
        assert normalize_polish_numbers("czterdziestu tysięcy") == "40000"
        assert normalize_polish_numbers("czterdziestoma tysiącami") == "40000"
    
    def test_fifty_thousand(self):
        assert normalize_polish_numbers("pięćdziesiąt tysięcy") == "50000"
        assert normalize_polish_numbers("pięćdziesięciu tysięcy") == "50000"
        assert normalize_polish_numbers("pięćdziesięcioma tysiącami") == "50000"
    
    def test_sixty_thousand(self):
        assert normalize_polish_numbers("sześćdziesiąt tysięcy") == "60000"
        assert normalize_polish_numbers("sześćdziesięciu tysięcy") == "60000"
        assert normalize_polish_numbers("sześćdziesięcioma tysiącami") == "60000"
    
    def test_seventy_thousand(self):
        assert normalize_polish_numbers("siedemdziesiąt tysięcy") == "70000"
        assert normalize_polish_numbers("siedemdziesięciu tysięcy") == "70000"
        assert normalize_polish_numbers("siedemdziesięcioma tysiącami") == "70000"
    
    def test_eighty_thousand(self):
        assert normalize_polish_numbers("osiemdziesiąt tysięcy") == "80000"
        assert normalize_polish_numbers("osiemdziesięciu tysięcy") == "80000"
        assert normalize_polish_numbers("osiemdziesięcioma tysiącami") == "80000"
    
    def test_ninety_thousand(self):
        assert normalize_polish_numbers("dziewięćdziesiąt tysięcy") == "90000"
        assert normalize_polish_numbers("dziewięćdziesięciu tysięcy") == "90000"
        assert normalize_polish_numbers("dziewięćdziesięcioma tysiącami") == "90000"


class TestCardinalNumbersWithoutDiacritics:
    
    def test_zero_without_diacritics(self):
        assert normalize_polish_numbers("zero") == "0"
    
    def test_fifteen_without_diacritics(self):
        assert normalize_polish_numbers("pietnascie") == "15"
        assert normalize_polish_numbers("pietnastu") == "15"
        assert normalize_polish_numbers("pietnastoma") == "15"
    
    def test_fifty_without_diacritics(self):
        assert normalize_polish_numbers("piecdziesiat") == "50"
        assert normalize_polish_numbers("piecdziesieciu") == "50"
        assert normalize_polish_numbers("piecdziesiecioma") == "50"
    
    def test_five_hundred_without_diacritics(self):
        assert normalize_polish_numbers("piecset") == "500"
        assert normalize_polish_numbers("pieciuset") == "500"
    
    def test_ten_thousand_without_diacritics(self):
        assert normalize_polish_numbers("dziesiec tysiecy") == "10000"
        assert normalize_polish_numbers("dziesieciu tysiecy") == "10000"
        assert normalize_polish_numbers("dziesiecioma tysiacami") == "10000"
    
    def test_twenty_five_thousand_without_diacritics(self):
        assert normalize_polish_numbers("dwadziescia piec tysiecy") == "25000"
        assert normalize_polish_numbers("dwudziestu pieciu tysiecy") == "25000"
