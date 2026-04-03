
import pytest
from src.normalizer import normalize_polish_numbers


class TestMixedText:
    
    def test_simple_mixed_text(self):
        assert normalize_polish_numbers("Mam 15 jabłek i dwadzieścia gruszek") == "Mam 15 jabłek i 20 gruszek"
        assert normalize_polish_numbers("To jest piętnasty rozdział, a to 20. strona") == "To jest 15 rozdział, a to 20. strona"
        assert normalize_polish_numbers("Spotkaliśmy się o godzinie 17:30 i piętnaście minut później") == "Spotkaliśmy się o godzinie 17:30 i 15 minut później"
        assert normalize_polish_numbers("Kupiłem 3 jabłka, dwieście gruszek i tysiąc śliwek") == "Kupiłem 3 jabłka, 200 gruszek i 1000 śliwek"
    
    def test_mixed_text_with_ten_thousands(self):
        assert normalize_polish_numbers("W firmie pracuje pięćdziesiąt tysięcy osób") == "W firmie pracuje 50000 osób"
        assert normalize_polish_numbers("Przejechaliśmy dwadzieścia pięć tysięcy kilometrów") == "Przejechaliśmy 25000 kilometrów"
        assert normalize_polish_numbers("Mam 15 jabłek, dwadzieścia gruszek i pięćdziesiąt tysięcy wiśni") == "Mam 15 jabłek, 20 gruszek i 50000 wiśni"
    
    def test_mixed_text_with_ordinal_numbers(self):
        assert normalize_polish_numbers("zamieszkały na ósmej planecie") == "zamieszkały na 8 planecie"
        assert normalize_polish_numbers("To jest dwudziesty piąty przykład") == "To jest 25 przykład"
        assert normalize_polish_numbers("To jest pierwszy rozdział, a to drugi") == "To jest 1 rozdział, a to 2"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w drugim wyścigu") == "Zajęliśmy 5 miejsce w 2 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w trzecim wyścigu") == "Zajęliśmy 5 miejsce w 3 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w czwartym wyścigu") == "Zajęliśmy 5 miejsce w 4 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w piątym wyścigu") == "Zajęliśmy 5 miejsce w 5 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w szóstym wyścigu") == "Zajęliśmy 5 miejsce w 6 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w siódmym wyścigu") == "Zajęliśmy 5 miejsce w 7 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w ósmym wyścigu") == "Zajęliśmy 5 miejsce w 8 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w dziewiątym wyścigu") == "Zajęliśmy 5 miejsce w 9 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w dziesiątym wyścigu") == "Zajęliśmy 5 miejsce w 10 wyścigu"
        assert normalize_polish_numbers("Zajęliśmy piąte miejsce w pierwszym wyścigu") == "Zajęliśmy 5 miejsce w 1 wyścigu"

        
    
    def test_mixed_text_with_compound_numbers(self):
        assert normalize_polish_numbers("Mam pięćset dwadzieścia trzy jabłka") == "Mam 523 jabłka"
        assert normalize_polish_numbers("Dwa tysiące trzysta czterdzieści pięć osób wzięło udział") == "2345 osób wzięło udział"
        assert normalize_polish_numbers("Trzydzieści cztery tysiące pięćset sześćdziesiąt siedem złotych") == "34567 złotych"
    
    def test_mixed_text_with_digits_and_words(self):
        assert normalize_polish_numbers("Mam 15 jabłek i dwadzieścia gruszek") == "Mam 15 jabłek i 20 gruszek"
        assert normalize_polish_numbers("To jest 15. rozdział, a to dwudziesty") == "To jest 15. rozdział, a to 20"
        assert normalize_polish_numbers("Spotkaliśmy się o 17:30 i piętnaście minut później") == "Spotkaliśmy się o 17:30 i 15 minut później"
    
    def test_mixed_text_with_punctuation(self):
        assert normalize_polish_numbers("Mam pięć jabłek, trzy gruszki i dwanaście śliwek.") == "Mam 5 jabłek, 3 gruszki i 12 śliwek."
        assert normalize_polish_numbers("To jest pierwszy, drugi i trzeci przykład!") == "To jest 1, 2 i 3 przykład!"
        assert normalize_polish_numbers("Czy masz dwadzieścia pięć złotych?") == "Czy masz 25 złotych?"
    
    def test_mixed_text_with_mixed_diacritics(self):
        assert normalize_polish_numbers("Mam piec jabłek i pięć gruszek") == "Mam 5 jabłek i 5 gruszek"
        assert normalize_polish_numbers("To jest pietnasty i piętnasty rozdział") == "To jest 15 i 15 rozdział"
        assert normalize_polish_numbers("Dwadziescia piec i dwadzieścia pięć") == "25 i 25"


class TestEdgeCases:
    
    def test_number_at_beginning(self):
        assert normalize_polish_numbers("Pięć jabłek") == "5 jabłek"
        assert normalize_polish_numbers("Dwadzieścia trzy gruszki") == "23 gruszki"
        assert normalize_polish_numbers("Tysiąc osób") == "1000 osób"
    
    def test_number_at_end(self):
        assert normalize_polish_numbers("Mam pięć") == "Mam 5"
        assert normalize_polish_numbers("To jest dwadzieścia trzy") == "To jest 23"
        assert normalize_polish_numbers("Zgromadzono tysiąc") == "Zgromadzono 1000"
    
    def test_multiple_consecutive_numbers(self):
        assert normalize_polish_numbers("jeden dwa trzy") == "1 2 3"
        assert normalize_polish_numbers("pięć dziesięć piętnaście dwadzieścia") == "5 10 15 20"
        assert normalize_polish_numbers("sto dwieście trzysta") == "100 200 300"
    
    def test_single_number_only(self):
        assert normalize_polish_numbers("pięć") == "5"
        assert normalize_polish_numbers("dwadzieścia trzy") == "23"
        assert normalize_polish_numbers("tysiąc") == "1000"
    
    def test_empty_string(self):
        assert normalize_polish_numbers("") == ""
    
    def test_no_numbers(self):
        assert normalize_polish_numbers("To jest przykładowy tekst") == "To jest przykładowy tekst"
        assert normalize_polish_numbers("Brak liczb w tym zdaniu") == "Brak liczb w tym zdaniu"
    
    def test_numbers_already_as_digits(self):
        assert normalize_polish_numbers("Mam 15 jabłek") == "Mam 15 jabłek"
        assert normalize_polish_numbers("To jest 123.45") == "To jest 123.45"
        assert normalize_polish_numbers("17:30") == "17:30"
    
    def test_hyphenated_compounds(self):
        assert normalize_polish_numbers("dwadzieścia-trzy") == "20-3"
        assert normalize_polish_numbers("pięćset-dwadzieścia-trzy") == "500-20-3"
    
    def test_numbers_with_spaces(self):
        assert normalize_polish_numbers("pięć  dwadzieścia  trzy") == "5 23"  
        assert normalize_polish_numbers("sto  dwieście  trzysta") == "100 200 300"
    
    def test_case_sensitivity(self):
        assert normalize_polish_numbers("Pięć") == "5"
        assert normalize_polish_numbers("PIĘĆ") == "5"
        assert normalize_polish_numbers("pięĆ") == "5"
        assert normalize_polish_numbers("Dwadzieścia") == "20"
        assert normalize_polish_numbers("DWADZIEŚCIA") == "20"
        assert normalize_polish_numbers("dWaDzIeŚcIa") == "20"


class TestSpecialCases:
    
    def test_zero(self):
        assert normalize_polish_numbers("zero") == "0"
        assert normalize_polish_numbers("Mam zero jabłek") == "Mam 0 jabłek"
        assert normalize_polish_numbers("Zerowa wartość") == "0 wartość"
    
    def test_large_numbers(self):
        assert normalize_polish_numbers("dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć") == "99999"
        assert normalize_polish_numbers("pięćdziesiąt tysięcy") == "50000"
        assert normalize_polish_numbers("osiemdziesiąt osiem tysięcy osiemset osiemdziesiąt osiem") == "88888"
    
    def test_numbers_in_quotes(self):
        assert normalize_polish_numbers('"pięć"') == '"5"'
        assert normalize_polish_numbers("'dwadzieścia trzy'") == "'23'"
        assert normalize_polish_numbers("(sto)") == "(100)"
    
    def test_numbers_with_time_format(self):
        assert normalize_polish_numbers("godzina piętnaście") == "godzina 15"
        assert normalize_polish_numbers("17:30") == "17:30"
        assert normalize_polish_numbers("piętnaście minut trzydziestą") == "15 minut 30"
    
    def test_numbers_with_percentages(self):
        assert normalize_polish_numbers("pięćdziesiąt procent") == "50 procent"
        assert normalize_polish_numbers("25%") == "25%"
        assert normalize_polish_numbers("dwadzieścia pięć %") == "25 %"
    
    def test_numbers_with_currencies(self):
        assert normalize_polish_numbers("pięć złotych") == "5 złotych"
        assert normalize_polish_numbers("sto euro") == "100 euro"
        assert normalize_polish_numbers("tysiąc dolarów") == "1000 dolarów"
    
    def test_numbers_with_units(self):
        assert normalize_polish_numbers("pięć metrów") == "5 metrów"
        assert normalize_polish_numbers("sto kilometrów") == "100 kilometrów"
        assert normalize_polish_numbers("tysiąc gramów") == "1000 gramów"
    
    def test_numbers_with_ordinals_and_units(self):
        assert normalize_polish_numbers("piąty piętro") == "5 piętro"
        assert normalize_polish_numbers("dziesiąta minuta") == "10 minuta"
        assert normalize_polish_numbers("setny metr") == "100 metr"
    
    def test_repeated_numbers(self):
        assert normalize_polish_numbers("pięć pięć pięć") == "5 5 5"
        assert normalize_polish_numbers("sto sto sto") == "100 100 100"
        assert normalize_polish_numbers("tysiąc tysiąc tysiąc") == "1000 1000 1000"
    
    def test_numbers_with_special_characters(self):
        assert normalize_polish_numbers("pięć@dwadzieścia") == "5@20"
        assert normalize_polish_numbers("sto#trzysta") == "100#300"
        assert normalize_polish_numbers("tysiąc&dwa") == "1000&2"


class TestRealWorldExamples:
    
    def test_news_headline(self):
        assert normalize_polish_numbers("Pięć osób zginęło w wypadku") == "5 osób zginęło w wypadku"
        assert normalize_polish_numbers("Dwadzieścia pięć tysięcy osób wzięło udział w proteście") == "25000 osób wzięło udział w proteście"
    
    def test_recipe(self):
        assert normalize_polish_numbers("Potrzebujesz pięć jajek, dwieście gramów mąki i sto mililitrów mleka") == "Potrzebujesz 5 jajek, 200 gramów mąki i 100 mililitrów mleka"
        assert normalize_polish_numbers("Piecz przez trzydzieści minut") == "Piecz przez 30 minut"
    
    def test_sports_results(self):
        assert normalize_polish_numbers("Polska wygrała trzy do jednego") == "Polska wygrała 3 do 1"
        assert normalize_polish_numbers("To był pięćdziesiąty mecz w sezonie") == "To był 50 mecz w sezonie"
    
    def test_scientific_data(self):
        assert normalize_polish_numbers("Przebadano pięćset osób") == "Przebadano 500 osób"
        assert normalize_polish_numbers("Wyniki pokazują, że dziewięćdziesiąt procent badanych") == "Wyniki pokazują, że 90 procent badanych"
    
    def test_financial_report(self):
        assert normalize_polish_numbers("Przychód wyniósł pięćdziesiąt tysięcy złotych") == "Przychód wyniósł 50000 złotych"
        assert normalize_polish_numbers("Zysk wzrósł o dwadzieścia pięć procent") == "Zysk wzrósł o 25 procent"
    
    def test_address(self):
        assert normalize_polish_numbers("Ulica Piąta, numer dwadzieścia trzy") == "Ulica 5, numer 23"
        assert normalize_polish_numbers("Mieszkanie piętnaście") == "Mieszkanie 15"
    
    def test_date(self):
        assert normalize_polish_numbers("piętnasty marca") == "15 marca"
        assert normalize_polish_numbers("dwudziesty piąty grudnia") == "25 grudnia"
        assert normalize_polish_numbers("rok dwa tysiące dwadzieścia cztery") == "rok 2024"


class TestCompoundingRules:
    
    def test_teen_tens_with_regular_tens(self):
        assert normalize_polish_numbers("dziesięć dwadzieścia") == "10 20"
        assert normalize_polish_numbers("jedenaście trzydzieści") == "11 30"
        assert normalize_polish_numbers("piętnaście czterdzieści") == "15 40"
        assert normalize_polish_numbers("dziewiętnaście pięćdziesiąt") == "19 50"
    
    def test_regular_tens_with_teen_tens(self):
        assert normalize_polish_numbers("dwadzieścia dziesięć") == "20 10"
        assert normalize_polish_numbers("trzydzieści jedenaście") == "30 11"
        assert normalize_polish_numbers("czterdzieści piętnaście") == "40 15"
        assert normalize_polish_numbers("pięćdziesiąt dziewiętnaście") == "50 19"
    
    def test_units_with_teen_tens(self):
        assert normalize_polish_numbers("jeden dziesięć") == "1 10"
        assert normalize_polish_numbers("dwa jedenaście") == "2 11"
        assert normalize_polish_numbers("pięć piętnaście") == "5 15"
        assert normalize_polish_numbers("dziewięć dziewiętnaście") == "9 19"
    
    def test_teen_tens_with_units(self):
        assert normalize_polish_numbers("dziesięć jeden") == "10 1"
        assert normalize_polish_numbers("jedenaście dwa") == "11 2"
        assert normalize_polish_numbers("piętnaście pięć") == "15 5"
        assert normalize_polish_numbers("dziewiętnaście dziewięć") == "19 9"
    
    def test_multiple_teen_tens(self):
        assert normalize_polish_numbers("dziesięć jedenaście dwanaście") == "10 11 12"
        assert normalize_polish_numbers("trzynaście czternaście piętnaście") == "13 14 15"
        assert normalize_polish_numbers("szesnaście siedemnaście osiemnaście") == "16 17 18"
    
    def test_hundreds_with_teen_tens(self):
        assert normalize_polish_numbers("sto dziesięć") == "110"
        assert normalize_polish_numbers("dwieście jedenaście") == "211"
        assert normalize_polish_numbers("pięćset piętnaście") == "515"
        assert normalize_polish_numbers("sześćset dziewiętnaście") == "619"
    
    def test_thousands_with_teen_tens(self):
        assert normalize_polish_numbers("tysiąc dziesięć") == "1010"
        assert normalize_polish_numbers("dwa tysiące jedenaście") == "2011"
        assert normalize_polish_numbers("pięć tysięcy piętnaście") == "5015"
    
    def test_units_with_regular_tens(self):
        assert normalize_polish_numbers("trzy dwadzieścia") == "3 20"
        assert normalize_polish_numbers("pięć trzydzieści") == "5 30"
        assert normalize_polish_numbers("siedem czterdzieści") == "7 40"
        assert normalize_polish_numbers("dziewięć pięćdziesiąt") == "9 50"
    
    def test_regular_tens_with_units(self):
        assert normalize_polish_numbers("dwadzieścia trzy") == "23"
        assert normalize_polish_numbers("trzydzieści pięć") == "35"
        assert normalize_polish_numbers("czterdzieści siedem") == "47"
        assert normalize_polish_numbers("pięćdziesiąt dziewięć") == "59"
    
    def test_hundreds_with_regular_tens(self):
        assert normalize_polish_numbers("sto dwadzieścia") == "120"
        assert normalize_polish_numbers("dwieście trzydzieści") == "230"
        assert normalize_polish_numbers("pięćset czterdzieści") == "540"
    
    def test_hundreds_with_units(self):
        assert normalize_polish_numbers("sto jeden") == "101"
        assert normalize_polish_numbers("dwieście pięć") == "205"
        assert normalize_polish_numbers("pięćset dziewięć") == "509"
    
    def test_complex_mixed_sequences(self):
        assert normalize_polish_numbers("pięć dziesięć dwadzieścia trzy") == "5 10 23"
        assert normalize_polish_numbers("sto piętnaście dwadzieścia") == "115 20"
        assert normalize_polish_numbers("tysiąc dziesięć dwadzieścia") == "1010 20"
        assert normalize_polish_numbers("pięćset piętnaście dwadzieścia trzy") == "515 23"
    
    def test_same_order_magnitude(self):
        assert normalize_polish_numbers("sto dwieście trzysta") == "100 200 300"
        assert normalize_polish_numbers("pięćset sześćset siedemset") == "500 600 700"
        
        assert normalize_polish_numbers("dwadzieścia trzydzieści czterdzieści") == "20 30 40"
        assert normalize_polish_numbers("pięćdziesiąt sześćdziesiąt siedemdziesiąt") == "50 60 70"
        
        assert normalize_polish_numbers("jeden dwa trzy") == "1 2 3"
        assert normalize_polish_numbers("cztery pięć sześć") == "4 5 6"
    
    def test_smaller_before_larger_magnitude(self):
        assert normalize_polish_numbers("pięć sto") == "5 100"
        assert normalize_polish_numbers("trzy dwieście") == "3 200"
        
        assert normalize_polish_numbers("dwadzieścia sto") == "20 100"
        assert normalize_polish_numbers("trzydzieści dwieście") == "30 200"
        
        assert normalize_polish_numbers("dziesięć sto") == "10 100"
        assert normalize_polish_numbers("piętnaście dwieście") == "15 200"
        
        assert normalize_polish_numbers("dwa tysiące") == "2000"

        assert normalize_polish_numbers("pięć tysiąc") == "5 1000"

        assert normalize_polish_numbers("pięć dwa tysiące dwa") == "5 2002"

        assert normalize_polish_numbers("tysiące") == "tysiące"