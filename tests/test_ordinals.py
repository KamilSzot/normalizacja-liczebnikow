import pytest
from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestOrdinalNumbers1to19:
    def test_first(self):
        assert normalize_polish_numbers("pierwszy") == "1"
        assert normalize_polish_numbers("pierwsza") == "1"
        assert normalize_polish_numbers("pierwsze") == "1"

    def test_second(self):
        assert normalize_polish_numbers("drugi") == "2"
        assert normalize_polish_numbers("druga") == "2"
        assert normalize_polish_numbers("drugie") == "2"

    def test_third(self):
        assert normalize_polish_numbers("trzeci") == "3"
        assert normalize_polish_numbers("trzecia") == "3"
        assert normalize_polish_numbers("trzecie") == "3"

    def test_fourth(self):
        assert normalize_polish_numbers("czwarty") == "4"
        assert normalize_polish_numbers("czwarta") == "4"
        assert normalize_polish_numbers("czwarte") == "4"

    def test_fifth(self):
        assert normalize_polish_numbers("piąty") == "5"
        assert normalize_polish_numbers("piąta") == "5"
        assert normalize_polish_numbers("piąte") == "5"

    def test_sixth(self):
        assert normalize_polish_numbers("szósty") == "6"
        assert normalize_polish_numbers("szósta") == "6"
        assert normalize_polish_numbers("szóste") == "6"

    def test_seventh(self):
        assert normalize_polish_numbers("siódmy") == "7"
        assert normalize_polish_numbers("siódma") == "7"
        assert normalize_polish_numbers("siódme") == "7"

    def test_eighth(self):
        assert normalize_polish_numbers("ósmy") == "8"
        assert normalize_polish_numbers("ósma") == "8"
        assert normalize_polish_numbers("ósme") == "8"

    def test_ninth(self):
        assert normalize_polish_numbers("dziewiąty") == "9"
        assert normalize_polish_numbers("dziewiąta") == "9"
        assert normalize_polish_numbers("dziewiąte") == "9"

    def test_tenth(self):
        assert normalize_polish_numbers("dziesiąty") == "10"
        assert normalize_polish_numbers("dziesiąta") == "10"
        assert normalize_polish_numbers("dziesiąte") == "10"

    def test_eleventh(self):
        assert normalize_polish_numbers("jedenasty") == "11"
        assert normalize_polish_numbers("jedenasta") == "11"
        assert normalize_polish_numbers("jedenaste") == "11"

    def test_twelfth(self):
        assert normalize_polish_numbers("dwunasty") == "12"
        assert normalize_polish_numbers("dwunasta") == "12"
        assert normalize_polish_numbers("dwunaste") == "12"

    def test_thirteenth(self):
        assert normalize_polish_numbers("trzynasty") == "13"
        assert normalize_polish_numbers("trzynasta") == "13"
        assert normalize_polish_numbers("trzynaste") == "13"

    def test_fourteenth(self):
        assert normalize_polish_numbers("czternasty") == "14"
        assert normalize_polish_numbers("czternasta") == "14"
        assert normalize_polish_numbers("czternaste") == "14"

    def test_fifteenth(self):
        assert normalize_polish_numbers("piętnasty") == "15"
        assert normalize_polish_numbers("piętnasta") == "15"
        assert normalize_polish_numbers("piętnaste") == "15"

    def test_sixteenth(self):
        assert normalize_polish_numbers("szesnasty") == "16"
        assert normalize_polish_numbers("szesnasta") == "16"
        assert normalize_polish_numbers("szesnaste") == "16"

    def test_seventeenth(self):
        assert normalize_polish_numbers("siedemnasty") == "17"
        assert normalize_polish_numbers("siedemnasta") == "17"
        assert normalize_polish_numbers("siedemnaste") == "17"

    def test_eighteenth(self):
        assert normalize_polish_numbers("osiemnasty") == "18"
        assert normalize_polish_numbers("osiemnasta") == "18"
        assert normalize_polish_numbers("osiemnaste") == "18"

    def test_nineteenth(self):
        assert normalize_polish_numbers("dziewiętnasty") == "19"
        assert normalize_polish_numbers("dziewiętnasta") == "19"
        assert normalize_polish_numbers("dziewiętnaste") == "19"


class TestOrdinalNumbersTens:
    def test_twentieth(self):
        assert normalize_polish_numbers("dwudziesty") == "20"
        assert normalize_polish_numbers("dwudziesta") == "20"
        assert normalize_polish_numbers("dwudzieste") == "20"

    def test_thirtieth(self):
        assert normalize_polish_numbers("trzydziesty") == "30"
        assert normalize_polish_numbers("trzydziesta") == "30"
        assert normalize_polish_numbers("trzydzieste") == "30"

    def test_fortieth(self):
        assert normalize_polish_numbers("czterdziesty") == "40"
        assert normalize_polish_numbers("czterdziesta") == "40"
        assert normalize_polish_numbers("czterdzieste") == "40"

    def test_fiftieth(self):
        assert normalize_polish_numbers("pięćdziesiąty") == "50"
        assert normalize_polish_numbers("pięćdziesiąta") == "50"
        assert normalize_polish_numbers("pięćdziesiąte") == "50"

    def test_sixtieth(self):
        assert normalize_polish_numbers("sześćdziesiąty") == "60"
        assert normalize_polish_numbers("sześćdziesiąta") == "60"
        assert normalize_polish_numbers("sześćdziesiąte") == "60"

    def test_seventieth(self):
        assert normalize_polish_numbers("siedemdziesiąty") == "70"
        assert normalize_polish_numbers("siedemdziesiąta") == "70"
        assert normalize_polish_numbers("siedemdziesiąte") == "70"

    def test_eightieth(self):
        assert normalize_polish_numbers("osiemdziesiąty") == "80"
        assert normalize_polish_numbers("osiemdziesiąta") == "80"
        assert normalize_polish_numbers("osiemdziesiąte") == "80"

    def test_ninetieth(self):
        assert normalize_polish_numbers("dziewięćdziesiąty") == "90"
        assert normalize_polish_numbers("dziewięćdziesiąta") == "90"
        assert normalize_polish_numbers("dziewięćdziesiąte") == "90"


class TestOrdinalNumbersHundreds:
    def test_hundredth(self):
        assert normalize_polish_numbers("setny") == "100"
        assert normalize_polish_numbers("setna") == "100"
        assert normalize_polish_numbers("setne") == "100"

    def test_two_hundredth(self):
        assert normalize_polish_numbers("dwusetny") == "200"
        assert normalize_polish_numbers("dwóchsetny") == "200"

        assert normalize_polish_numbers("dwuseta") == "200"
        assert normalize_polish_numbers("dwusete") == "200"

    def test_three_hundredth(self):
        assert normalize_polish_numbers("trzechsetny") == "300"
        assert normalize_polish_numbers("trzechsetna") == "300"
        assert normalize_polish_numbers("trzechsetne") == "300"

    def test_four_hundredth(self):
        assert normalize_polish_numbers("czterechsetny") == "400"
        assert normalize_polish_numbers("czterechsetna") == "400"
        assert normalize_polish_numbers("czterechsetne") == "400"

    def test_five_hundredth(self):
        assert normalize_polish_numbers("pięćsetny") == "500"
        assert normalize_polish_numbers("pięćsetna") == "500"
        assert normalize_polish_numbers("pięćsetne") == "500"

    def test_six_hundredth(self):
        assert normalize_polish_numbers("sześćsetny") == "600"
        assert normalize_polish_numbers("sześćsetna") == "600"
        assert normalize_polish_numbers("sześćsetne") == "600"

    def test_seven_hundredth(self):
        assert normalize_polish_numbers("siedemsetny") == "700"
        assert normalize_polish_numbers("siedemsetna") == "700"
        assert normalize_polish_numbers("siedemsetne") == "700"

    def test_eight_hundredth(self):
        assert normalize_polish_numbers("osiemsetny") == "800"
        assert normalize_polish_numbers("osiemsetna") == "800"
        assert normalize_polish_numbers("osiemsetne") == "800"

    def test_nine_hundredth(self):
        assert normalize_polish_numbers("dziewięćsetny") == "900"
        assert normalize_polish_numbers("dziewięćsetna") == "900"
        assert normalize_polish_numbers("dziewięćsetne") == "900"


class TestOrdinalNumbersThousands:
    def test_thousandth(self):
        assert normalize_polish_numbers("tysięczny") == "1000"
        assert normalize_polish_numbers("tysięczna") == "1000"
        assert normalize_polish_numbers("tysięczne") == "1000"

    def test_two_thousandth(self):
        assert normalize_polish_numbers("dwutysięczny") == "2000"
        assert normalize_polish_numbers("dwutysięczna") == "2000"
        assert normalize_polish_numbers("dwutysięczne") == "2000"

    def test_three_thousandth(self):
        assert normalize_polish_numbers("trzytysięczny") == "3000"
        assert normalize_polish_numbers("trzytysięczna") == "3000"
        assert normalize_polish_numbers("trzytysięczne") == "3000"

    def test_four_thousandth(self):
        assert normalize_polish_numbers("cztertysięczny") == "4000"
        assert normalize_polish_numbers("cztertysięczna") == "4000"
        assert normalize_polish_numbers("cztertysięczne") == "4000"

    def test_five_thousandth(self):
        assert normalize_polish_numbers("pięciotysięczny") == "5000"
        assert normalize_polish_numbers("pięciotysięczna") == "5000"
        assert normalize_polish_numbers("pięciotysięczne") == "5000"

    def test_six_thousandth(self):
        assert normalize_polish_numbers("sześciotysięczny") == "6000"
        assert normalize_polish_numbers("sześciotysięczna") == "6000"
        assert normalize_polish_numbers("sześciotysięczne") == "6000"

    def test_seven_thousandth(self):
        assert normalize_polish_numbers("siedmiotysięczny") == "7000"
        assert normalize_polish_numbers("siedmiotysięczna") == "7000"
        assert normalize_polish_numbers("siedmiotysięczne") == "7000"

    def test_eight_thousandth(self):
        assert normalize_polish_numbers("ośmiotysięczny") == "8000"
        assert normalize_polish_numbers("ośmiotysięczna") == "8000"
        assert normalize_polish_numbers("ośmiotysięczne") == "8000"

    def test_nine_thousandth(self):
        assert normalize_polish_numbers("dziewięciotysięczny") == "9000"
        assert normalize_polish_numbers("dziewięciotysięczna") == "9000"
        assert normalize_polish_numbers("dziewięciotysięczne") == "9000"


class TestOrdinalNumbersTenThousands:
    def test_ten_thousandth(self):
        assert normalize_polish_numbers("dziesięciotysięczny") == "10000"
        assert normalize_polish_numbers("dziesięciotysięczna") == "10000"
        assert normalize_polish_numbers("dziesięciotysięczne") == "10000"

    def test_twenty_thousandth(self):
        assert normalize_polish_numbers("dwudziestotysięczny") == "20000"
        assert normalize_polish_numbers("dwudziestotysięczna") == "20000"
        assert normalize_polish_numbers("dwudziestotysięczne") == "20000"

    def test_thirty_thousandth(self):
        assert normalize_polish_numbers("trzydziestotysięczny") == "30000"
        assert normalize_polish_numbers("trzydziestotysięczna") == "30000"
        assert normalize_polish_numbers("trzydziestotysięczne") == "30000"

    def test_forty_thousandth(self):
        assert normalize_polish_numbers("czterdziestotysięczny") == "40000"
        assert normalize_polish_numbers("czterdziestotysięczna") == "40000"
        assert normalize_polish_numbers("czterdziestotysięczne") == "40000"

    def test_fifty_thousandth(self):
        assert normalize_polish_numbers("pięćdziesięciotysięczny") == "50000"
        assert normalize_polish_numbers("pięćdziesięciotysięczna") == "50000"
        assert normalize_polish_numbers("pięćdziesięciotysięczne") == "50000"

    def test_sixty_thousandth(self):
        assert normalize_polish_numbers("sześćdziesięciotysięczny") == "60000"
        assert normalize_polish_numbers("sześćdziesięciotysięczna") == "60000"
        assert normalize_polish_numbers("sześćdziesięciotysięczne") == "60000"

    def test_seventy_thousandth(self):
        assert normalize_polish_numbers("siedemdziesięciotysięczny") == "70000"
        assert normalize_polish_numbers("siedemdziesięciotysięczna") == "70000"
        assert normalize_polish_numbers("siedemdziesięciotysięczne") == "70000"

    def test_eighty_thousandth(self):
        assert normalize_polish_numbers("osiemdziesięciotysięczny") == "80000"
        assert normalize_polish_numbers("osiemdziesięciotysięczna") == "80000"
        assert normalize_polish_numbers("osiemdziesięciotysięczne") == "80000"

    def test_ninety_thousandth(self):
        assert normalize_polish_numbers("dziewięćdziesięciotysięczny") == "90000"
        assert normalize_polish_numbers("dziewięćdziesięciotysięczna") == "90000"
        assert normalize_polish_numbers("dziewięćdziesięciotysięczne") == "90000"


class TestOrdinalNumbersWithoutDiacritics:
    def test_fifth_without_diacritics(self):
        assert normalize_polish_numbers("piaty") == "5"
        assert normalize_polish_numbers("piata") == "5"
        assert normalize_polish_numbers("piate") == "5"

    def test_fifteenth_without_diacritics(self):
        assert normalize_polish_numbers("pietnasty") == "15"
        assert normalize_polish_numbers("pietnasta") == "15"
        assert normalize_polish_numbers("pietnaste") == "15"

    def test_fiftieth_without_diacritics(self):
        assert normalize_polish_numbers("piecdziesiaty") == "50"
        assert normalize_polish_numbers("piecdziesiata") == "50"
        assert normalize_polish_numbers("piecdziesiate") == "50"

    def test_five_hundredth_without_diacritics(self):
        assert normalize_polish_numbers("piecsetny") == "500"
        assert normalize_polish_numbers("piecsetna") == "500"
        assert normalize_polish_numbers("piecsetne") == "500"

    def test_ten_thousandth_without_diacritics(self):
        assert normalize_polish_numbers("dziesieciotysieczny") == "10000"
        assert normalize_polish_numbers("dziesieciotysieczna") == "10000"
        assert normalize_polish_numbers("dziesieciotysieczne") == "10000"

    def test_twenty_five_thousandth_without_diacritics(self):
        assert normalize_polish_numbers("dwudziestopięciotysieczny") == "25000"
        assert normalize_polish_numbers("dwudziestopieciotysieczny") == "25000"

    def test_huge(self):
        assert normalize_polish_numbers("sto tysięcy tysięczny") == "101000"
        assert normalize_polish_numbers("sto tysięcy dwutysięczny") == "102000"
        assert normalize_polish_numbers("sto dwadzieścia tysięcy tysięczny") == "121000"
        assert (
            normalize_polish_numbers("sto dwadzieścia tysięcy dwutysięczny") == "122000"
        )
