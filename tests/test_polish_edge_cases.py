import pytest

from normalizacja_liczebnikow.normalizer import normalize_polish_numbers


class TestSentenceLevelPolishCases:
    def test_declined_ordinals_inside_sentence(self):
        assert (
            normalize_polish_numbers("Mówiłem o ósmej planecie i dwudziestym rozdziale.")
            == "Mówiłem o 8 planecie i 20 rozdziale."
        )

    def test_compound_ordinal_in_oblique_case(self):
        assert (
            normalize_polish_numbers("O dwudziestym piątym rozdziale mówiliśmy wczoraj")
            == "O 25 rozdziale mówiliśmy wczoraj"
        )

    def test_feminine_declined_ordinals_in_coordination(self):
        assert (
            normalize_polish_numbers("Z pierwszą i drugą próbą się udało")
            == "Z 1 i 2 próbą się udało"
        )

    def test_declined_ordinals_with_existing_digit(self):
        assert (
            normalize_polish_numbers("To było w 3. albo czwartym dniu")
            == "To było w 3. albo 4 dniu"
        )

    def test_multiple_bracket_types(self):
        assert normalize_polish_numbers("(pięciu) [sześciu] {siedmiu}") == "(5) [6] {7}"

    def test_sentence_with_question_and_exclamation(self):
        assert normalize_polish_numbers("Dwa tysiące? Nie, trzy tysiące!") == "2000? Nie, 3000!"


class TestThousandCasesInSentences:
    def test_instrumental_thousands_in_sentence(self):
        assert (
            normalize_polish_numbers("Pomiędzy dwoma tysiącami a trzema tysiącami osób")
            == "Pomiędzy 2000 a 3000 osób"
        )

    def test_genitive_thousands_with_hundreds(self):
        assert (
            normalize_polish_numbers("Widziałem około pięciu tysięcy siedmiuset ludzi")
            == "Widziałem około 5700 ludzi"
        )

    def test_long_oblique_cardinal_phrase(self):
        assert (
            normalize_polish_numbers("Po tysiącu trzystu dwudziestu dniach")
            == "Po 1320 dniach"
        )


class TestParentheticalCompoundNumbers:
    def test_parenthesized_compound_ordinal(self):
        assert (
            normalize_polish_numbers("Rozdział (dwudziesty trzeci) był najkrótszy")
            == "Rozdział (23) był najkrótszy"
        )


class TestKnownAmbiguousSequences:

    def test_thousand_first_as_ordinal(self):
        assert normalize_polish_numbers("tysiąc pierwszy") == "1001"


    def test_two_thousand_first_as_ordinal(self):
        assert normalize_polish_numbers("dwa tysiące pierwszy") == "2001"


    def test_year_phrase_with_ordinal_tail(self):
        assert (
            normalize_polish_numbers("rok tysiąc dziewięćset osiemdziesiąty dziewiąty")
            == "rok 1989"
        )

    def test_hundred_eighty_second(self):
        assert normalize_polish_numbers("sto osiemdziesiąty drugi") == "182"


    def test_two_thousand_twenty_first(self):
        assert normalize_polish_numbers("dwa tysiące dwudziesty pierwszy") == "2021"

        
class TestFurtherAmbiguityLimitations:
    @pytest.mark.xfail(
        strict=True,
        reason="Fractional expressions like 'dwa i pół tysiąca' are not composed into a single quantity yet.",
    )
    def test_two_and_half_thousand(self):
        assert normalize_polish_numbers("dwa i pół tysiąca") == "2500"

    @pytest.mark.xfail(
        strict=True,
        reason="Lexicalized half forms such as 'półtora tysiąca' are not parsed yet.",
    )
    def test_one_and_half_thousand(self):
        assert normalize_polish_numbers("półtora tysiąca") == "1500"

    @pytest.mark.xfail(
        strict=True,
        reason="Range-like ellipsis is interpreted literally instead of expanding both thousand values.",
    )
    def test_range_of_thousands_with_shared_noun(self):
        assert normalize_polish_numbers("od pięciu do siedmiu tysięcy") == "od 5000 do 7000"

    @pytest.mark.xfail(
        strict=True,
        reason="Elliptic coordination after a composed number is not propagated to the second conjunct.",
    )
    def test_hundreds_with_elliptic_second_value(self):
        assert normalize_polish_numbers("dwieście trzy lub cztery osoby") == "203 lub 204 osoby"

    @pytest.mark.xfail(
        strict=True,
        reason="The parser does not reuse the composed prefix for abbreviated year coordination.",
    )
    def test_coordinated_year_phrase_with_elided_prefix(self):
        assert (
            normalize_polish_numbers(
                "w latach tysiąc dziewięćset osiemdziesiąty dziewiąty i dziewięćdziesiąty"
            )
            == "w latach 1989 i 1990"
        )
