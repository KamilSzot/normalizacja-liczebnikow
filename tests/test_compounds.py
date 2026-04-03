
import pytest
from src.normalizer import normalize_polish_numbers


class TestCompoundNumbersHundreds:
    
    def test_one_hundred_one(self):
        assert normalize_polish_numbers("sto jeden") == "101"
        assert normalize_polish_numbers("sto jednego") == "101"
    
    def test_one_hundred_twenty_three(self):
        assert normalize_polish_numbers("sto dwadzieścia trzy") == "123"
        assert normalize_polish_numbers("stu dwudziestu trzech") == "123"
    
    def test_two_hundred_fifty(self):
        assert normalize_polish_numbers("dwieście pięćdziesiąt") == "250"
        assert normalize_polish_numbers("dwustu pięćdziesięciu") == "250"
    
    def test_three_hundred_seventy_eight(self):
        assert normalize_polish_numbers("trzysta siedemdziesiąt osiem") == "378"
        assert normalize_polish_numbers("trzystu siedemdziesięciu ośmiu") == "378"
    
    def test_four_hundred_ninety_nine(self):
        assert normalize_polish_numbers("czterysta dziewięćdziesiąt dziewięć") == "499"
        assert normalize_polish_numbers("czterystu dziewięćdziesięciu dziewięciu") == "499"
    
    def test_five_hundred_twenty(self):
        assert normalize_polish_numbers("pięćset dwadzieścia") == "520"
        assert normalize_polish_numbers("pięciuset dwudziestu") == "520"
    
    def test_six_hundred_fifteen(self):
        assert normalize_polish_numbers("sześćset piętnaście") == "615"
        assert normalize_polish_numbers("sześciuset piętnastu") == "615"
    
    def test_six_hundred_thirteen(self):
        assert normalize_polish_numbers("sześćset trzynaście") == "613"
        assert normalize_polish_numbers("sześciuset trzynastu") == "613"
    
    def test_six_hundred_fourteen(self):
        assert normalize_polish_numbers("sześćset czternaście") == "614"
        assert normalize_polish_numbers("sześciuset czternastu") == "614"
    
    def test_six_hundred_sixteen(self):
        assert normalize_polish_numbers("sześćset szesnaście") == "616"
        assert normalize_polish_numbers("sześciuset szesnastu") == "616"
    
    def test_six_hundred_seventeen(self):
        assert normalize_polish_numbers("sześćset siedemnaście") == "617"
        assert normalize_polish_numbers("sześciuset siedemnastu") == "617"
    
    def test_six_hundred_eighteen(self):
        assert normalize_polish_numbers("sześćset osiemnaście") == "618"
        assert normalize_polish_numbers("sześciuset osiemnastu") == "618"
    
    def test_six_hundred_nineteen(self):
        assert normalize_polish_numbers("sześćset dziewiętnaście") == "619"
        assert normalize_polish_numbers("sześciuset dziewiętnastu") == "619"
    
    def test_five_hundred_fifteen(self):
        assert normalize_polish_numbers("pięćset piętnaście") == "515"
        assert normalize_polish_numbers("pięciuset piętnastu") == "515"
    
    def test_seven_hundred_fifteen(self):
        assert normalize_polish_numbers("siedemset piętnaście") == "715"
        assert normalize_polish_numbers("siedmiuset piętnastu") == "715"
    
    def test_three_hundred_fifteen(self):
        assert normalize_polish_numbers("trzysta piętnaście") == "315"
        assert normalize_polish_numbers("trzystu piętnastu") == "315"
    
    def test_seven_hundred_thirty_four(self):
        assert normalize_polish_numbers("siedemset trzydzieści cztery") == "734"
        assert normalize_polish_numbers("siedmiuset trzydziestu czterech") == "734"
    
    def test_eight_hundred_eighty_eight(self):
        assert normalize_polish_numbers("osiemset osiemdziesiąt osiem") == "888"
        assert normalize_polish_numbers("ośmiuset osiemdziesięciu ośmiu") == "888"
    
    def test_nine_hundred_ninety_nine(self):
        assert normalize_polish_numbers("dziewięćset dziewięćdziesiąt dziewięć") == "999"
        assert normalize_polish_numbers("dziewięciuset dziewięćdziesięciu dziewięciu") == "999"


class TestCompoundNumbersThousands:
    
    def test_one_thousand_one(self):
        assert normalize_polish_numbers("tysiąc jeden") == "1001"
        assert normalize_polish_numbers("tysiąca jednego") == "1001"
    
    def test_one_thousand_two_hundred_fifty(self):
        assert normalize_polish_numbers("tysiąc dwieście pięćdziesiąt") == "1250"
        assert normalize_polish_numbers("tysiąca dwustu pięćdziesięciu") == "1250"
    
    def test_two_thousand_three_hundred_forty_five(self):
        assert normalize_polish_numbers("dwa tysiące trzysta czterdzieści pięć") == "2345"
        assert normalize_polish_numbers("dwóch tysięcy trzystu czterdziestu pięciu") == "2345"
    
    def test_three_thousand_six_hundred_seventy_eight(self):
        assert normalize_polish_numbers("trzy tysiące sześćset siedemdziesiąt osiem") == "3678"
        assert normalize_polish_numbers("trzech tysięcy sześciuset siedemdziesięciu ośmiu") == "3678"
    
    def test_four_thousand_nine_hundred_ninety_nine(self):
        assert normalize_polish_numbers("cztery tysiące dziewięćset dziewięćdziesiąt dziewięć") == "4999"
        assert normalize_polish_numbers("czterech tysięcy dziewięciuset dziewięćdziesięciu dziewięciu") == "4999"
    
    def test_five_thousand_one_hundred_twenty_three(self):
        assert normalize_polish_numbers("pięć tysięcy sto dwadzieścia trzy") == "5123"
        assert normalize_polish_numbers("pięciu tysięcy stu dwudziestu trzech") == "5123"
    
    def test_six_thousand_five_hundred(self):
        assert normalize_polish_numbers("sześć tysięcy pięćset") == "6500"
        assert normalize_polish_numbers("sześciu tysięcy pięciuset") == "6500"
    
    def test_seven_thousand_eight_hundred_ninety(self):
        assert normalize_polish_numbers("siedem tysięcy osiemset dziewięćdziesiąt") == "7890"
        assert normalize_polish_numbers("siedmiu tysięcy ośmiuset dziewięćdziesięciu") == "7890"
    
    def test_eight_thousand_nine_hundred_ninety_nine(self):
        assert normalize_polish_numbers("osiem tysięcy dziewięćset dziewięćdziesiąt dziewięć") == "8999"
        assert normalize_polish_numbers("ośmiu tysięcy dziewięciuset dziewięćdziesięciu dziewięciu") == "8999"
    
    def test_nine_thousand_nine_hundred_ninety_nine(self):
        assert normalize_polish_numbers("dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć") == "9999"
        assert normalize_polish_numbers("dziewięciu tysięcy dziewięciuset dziewięćdziesięciu dziewięciu") == "9999"


class TestCompoundNumbersTenThousands:
    
    def test_ten_thousand_one(self):
        assert normalize_polish_numbers("dziesięć tysięcy jeden") == "10001"
        assert normalize_polish_numbers("dziesięciu tysięcy jednego") == "10001"
    
    def test_ten_thousand_five_hundred(self):
        assert normalize_polish_numbers("dziesięć tysięcy pięćset") == "10500"
        assert normalize_polish_numbers("dziesięciu tysięcy pięciuset") == "10500"
    
    def test_twelve_thousand_three_hundred_forty_five(self):
        assert normalize_polish_numbers("dwanaście tysięcy trzysta czterdzieści pięć") == "12345"
        assert normalize_polish_numbers("dwunastu tysięcy trzystu czterdziestu pięciu") == "12345"
    
    def test_twenty_five_thousand(self):
        assert normalize_polish_numbers("dwadzieścia pięć tysięcy") == "25000"
        assert normalize_polish_numbers("dwudziestu pięciu tysięcy") == "25000"
    
    def test_twenty_five_thousand_six_hundred_seventy_eight(self):
        assert normalize_polish_numbers("dwadzieścia pięć tysięcy sześćset siedemdziesiąt osiem") == "25678"
        assert normalize_polish_numbers("dwudziestu pięciu tysięcy sześciuset siedemdziesięciu ośmiu") == "25678"
    
    def test_thirty_four_thousand_five_hundred_sixty_seven(self):
        assert normalize_polish_numbers("trzydzieści cztery tysiące pięćset sześćdziesiąt siedem") == "34567"
        assert normalize_polish_numbers("trzydziestu czterech tysięcy pięciuset sześćdziesięciu siedmiu") == "34567"
    
    def test_forty_five_thousand_six_hundred_seventy_eight(self):
        assert normalize_polish_numbers("czterdzieści pięć tysięcy sześćset siedemdziesiąt osiem") == "45678"
        assert normalize_polish_numbers("czterdziestu pięciu tysięcy sześciuset siedemdziesięciu ośmiu") == "45678"
    
    def test_fifty_six_thousand_seven_hundred_eighty_nine(self):
        assert normalize_polish_numbers("pięćdziesiąt sześć tysięcy siedemset osiemdziesiąt dziewięć") == "56789"
        assert normalize_polish_numbers("pięćdziesięciu sześciu tysięcy siedmiuset osiemdziesięciu dziewięciu") == "56789"
    
    def test_sixty_seven_thousand_eight_hundred_ninety(self):
        assert normalize_polish_numbers("sześćdziesiąt siedem tysięcy osiemset dziewięćdziesiąt") == "67890"
        assert normalize_polish_numbers("sześćdziesięciu siedmiu tysięcy ośmiuset dziewięćdziesięciu") == "67890"
    
    def test_seventy_eight_thousand_nine_hundred_one(self):
        assert normalize_polish_numbers("siedemdziesiąt osiem tysięcy dziewięćset jeden") == "78901"
        assert normalize_polish_numbers("siedemdziesięciu ośmiu tysięcy dziewięciuset jednego") == "78901"
    
    def test_eighty_nine_thousand_twenty_three(self):
        assert normalize_polish_numbers("osiemdziesiąt dziewięć tysięcy dwadzieścia trzy") == "89023"
        assert normalize_polish_numbers("osiemdziesięciu dziewięciu tysięcy dwudziestu trzech") == "89023"
    
    def test_ninety_nine_thousand_nine_hundred_ninety_nine(self):
        assert normalize_polish_numbers("dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć") == "99999"
        assert normalize_polish_numbers("dziewięćdziesięciu dziewięciu tysięcy dziewięciuset dziewięćdziesięciu dziewięciu") == "99999"


class TestCompoundNumbersWithoutDiacritics:
    
    def test_one_hundred_twenty_three_without_diacritics(self):
        assert normalize_polish_numbers("sto dwadziescia trzy") == "123"
        assert normalize_polish_numbers("stu dwudziestu trzech") == "123"
    
    def test_two_thousand_three_hundred_forty_five_without_diacritics(self):
        assert normalize_polish_numbers("dwa tysiace trzysta czterdziesci piec") == "2345"
        assert normalize_polish_numbers("dwoch tysiecy trzystu czterdziestu pieciu") == "2345"
    
    def test_twenty_five_thousand_without_diacritics(self):
        assert normalize_polish_numbers("dwadziescia piec tysiecy") == "25000"
        assert normalize_polish_numbers("dwudziestu pieciu tysiecy") == "25000"
    
    def test_thirty_four_thousand_five_hundred_sixty_seven_without_diacritics(self):
        assert normalize_polish_numbers("trzydziesci cztery tysiace piecset szescdziesiat siedem") == "34567"
        assert normalize_polish_numbers("trzydziestu czterech tysiecy pieciuset szescdziesiatu siedmiu") == "34500 szescdziesiatu 7"
    
    def test_fifty_six_thousand_seven_hundred_eighty_nine_without_diacritics(self):
        assert normalize_polish_numbers("piecdziesiat szesc tysiecy siedemset osiemdziesiat dziewiec") == "56789"
        assert normalize_polish_numbers("piecdziesiatu szesciu tysiecy siedmiuset osiemdziesiatu dziewieciu") == "piecdziesiatu 6700 osiemdziesiatu 9"
    
    def test_ninety_nine_thousand_nine_hundred_ninety_nine_without_diacritics(self):
        assert normalize_polish_numbers("dziewiecdziesiat dziewiec tysiecy dziewiecset dziewiecdziesiat dziewiec") == "99999"
        assert normalize_polish_numbers("dziewiecdziesiatu dziewieciu tysiecy dziewieciuset dziewiecdziesiatu dziewieciu") == "dziewiecdziesiatu 9900 dziewiecdziesiatu 9"


class TestCompoundNumbersMixed:
    
    def test_tens_and_units(self):
        assert normalize_polish_numbers("dwadzieścia trzy") == "23"
        assert normalize_polish_numbers("trzydzieści cztery") == "34"
        assert normalize_polish_numbers("czterdzieści pięć") == "45"
        assert normalize_polish_numbers("pięćdziesiąt sześć") == "56"
        assert normalize_polish_numbers("sześćdziesiąt siedem") == "67"
        assert normalize_polish_numbers("siedemdziesiąt osiem") == "78"
        assert normalize_polish_numbers("osiemdziesiąt dziewięć") == "89"
    
    def test_hundreds_and_tens(self):
        assert normalize_polish_numbers("sto dwadzieścia") == "120"
        assert normalize_polish_numbers("dwieście trzydzieści") == "230"
        assert normalize_polish_numbers("trzysta czterdzieści") == "340"
        assert normalize_polish_numbers("czterysta pięćdziesiąt") == "450"
        assert normalize_polish_numbers("pięćset sześćdziesiąt") == "560"
        assert normalize_polish_numbers("sześćset siedemdziesiąt") == "670"
        assert normalize_polish_numbers("siedemset osiemdziesiąt") == "780"
        assert normalize_polish_numbers("osiemset dziewięćdziesiąt") == "890"
    
    def test_hundreds_and_units(self):
        assert normalize_polish_numbers("sto jeden") == "101"
        assert normalize_polish_numbers("dwieście dwa") == "202"
        assert normalize_polish_numbers("trzysta trzy") == "303"
        assert normalize_polish_numbers("czterysta cztery") == "404"
        assert normalize_polish_numbers("pięćset pięć") == "505"
        assert normalize_polish_numbers("sześćset sześć") == "606"
        assert normalize_polish_numbers("siedemset siedem") == "707"
        assert normalize_polish_numbers("osiemset osiem") == "808"
        assert normalize_polish_numbers("dziewięćset dziewięć") == "909"
    
    def test_thousands_and_hundreds(self):
        assert normalize_polish_numbers("tysiąc sto") == "1100"
        assert normalize_polish_numbers("dwa tysiące dwieście") == "2200"
        assert normalize_polish_numbers("trzy tysiące trzysta") == "3300"
        assert normalize_polish_numbers("cztery tysiące czterysta") == "4400"
        assert normalize_polish_numbers("pięć tysięcy pięćset") == "5500"
        assert normalize_polish_numbers("sześć tysięcy sześćset") == "6600"
        assert normalize_polish_numbers("siedem tysięcy siedemset") == "7700"
        assert normalize_polish_numbers("osiem tysięcy osiemset") == "8800"
        assert normalize_polish_numbers("dziewięć tysięcy dziewięćset") == "9900"
    
    def test_ten_thousands_and_thousands(self):
        assert normalize_polish_numbers("dziesięć tysięcy tysiąc") == "10000 1000"
        assert normalize_polish_numbers("dwadzieścia tysięcy dwa tysiące") == "20000 2000"
        assert normalize_polish_numbers("trzydzieści tysięcy trzy tysiące") == "30000 3000"
        assert normalize_polish_numbers("czterdzieści tysięcy cztery tysiące") == "40000 4000"
        assert normalize_polish_numbers("pięćdziesiąt tysięcy pięć tysięcy") == "50000 5000"
        assert normalize_polish_numbers("sześćdziesiąt tysięcy sześć tysięcy") == "60000 6000"
        assert normalize_polish_numbers("siedemdziesiąt tysięcy siedem tysięcy") == "70000 7000"
        assert normalize_polish_numbers("osiemdziesiąt tysięcy osiem tysięcy") == "80000 8000"
        assert normalize_polish_numbers("dziewięćdziesiąt tysięcy dziewięć tysięcy") == "90000 9000"
