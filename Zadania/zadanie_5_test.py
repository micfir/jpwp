import pytest

from zadanie_5 import Ksiazka, Biblioteka


@pytest.fixture
def biblioteka():
    return Biblioteka()


def test_utworzenie_ksiazki():
    ksiazka = Ksiazka("Lalka", "Bolesław Prus")

    assert ksiazka.tytul == "Lalka"
    assert ksiazka.autor == "Bolesław Prus"
    assert ksiazka.wypozyczona is False


def test_nie_mozna_utworzyc_ksiazki_bez_tytulu():
    with pytest.raises(ValueError):
        Ksiazka("", "Bolesław Prus")


def test_nie_mozna_utworzyc_ksiazki_bez_autora():
    with pytest.raises(ValueError):
        Ksiazka("Lalka", "")


def test_dodanie_ksiazki_do_biblioteki(biblioteka):
    ksiazka = Ksiazka("Lalka", "Bolesław Prus")

    biblioteka.dodaj_ksiazke(ksiazka)

    assert len(biblioteka.ksiazki) == 1
    assert biblioteka.ksiazki[0].tytul == "Lalka"


def test_usuniecie_ksiazki_z_biblioteki(biblioteka):
    ksiazka = Ksiazka("Lalka", "Bolesław Prus")
    biblioteka.dodaj_ksiazke(ksiazka)

    biblioteka.usun_ksiazke("Lalka")

    assert len(biblioteka.ksiazki) == 0


def test_nie_mozna_usunac_nieistniejacej_ksiazki(biblioteka):
    with pytest.raises(ValueError):
        biblioteka.usun_ksiazke("Pan Tadeusz")


def test_wyszukiwanie_ksiazki_nie_rozroznia_wielkosci_liter(biblioteka):
    ksiazka = Ksiazka("Lalka", "Bolesław Prus")
    biblioteka.dodaj_ksiazke(ksiazka)

    wynik = biblioteka.znajdz_ksiazke("lalka")

    assert wynik is ksiazka

def test_wypozyczenie_ksiazki(biblioteka):
    ksiazka = Ksiazka("Lalka", "Bolesław Prus")
    biblioteka.dodaj_ksiazke(ksiazka)

    biblioteka.wypozycz_ksiazke("Lalka")

    assert ksiazka.wypozyczona is True


def test_nie_mozna_wypozyczyc_nieistniejacej_ksiazki(biblioteka):
    with pytest.raises(ValueError):
        biblioteka.wypozycz_ksiazke("Pan Tadeusz")


def test_nie_mozna_wypozyczyc_ksiazki_drugi_raz(biblioteka):
    ksiazka = Ksiazka("Lalka", "Bolesław Prus")
    biblioteka.dodaj_ksiazke(ksiazka)

    biblioteka.wypozycz_ksiazke("Lalka")

    with pytest.raises(ValueError):
        biblioteka.wypozycz_ksiazke("Lalka")


def test_zwrot_ksiazki(biblioteka):
    ksiazka = Ksiazka("Lalka", "Bolesław Prus")
    biblioteka.dodaj_ksiazke(ksiazka)

    biblioteka.wypozycz_ksiazke("Lalka")
    biblioteka.zwroc_ksiazke("Lalka")

    assert ksiazka.wypozyczona is False


def test_nie_mozna_zwrocic_ksiazki_ktora_nie_byla_wypozyczona(biblioteka):
    ksiazka = Ksiazka("Lalka", "Bolesław Prus")
    biblioteka.dodaj_ksiazke(ksiazka)

    with pytest.raises(ValueError):
        biblioteka.zwroc_ksiazke("Lalka")


def test_lista_dostepnych_ksiazek(biblioteka):
    ksiazka_1 = Ksiazka("Lalka", "Bolesław Prus")
    ksiazka_2 = Ksiazka("Dziady", "Adam Mickiewicz")

    biblioteka.dodaj_ksiazke(ksiazka_1)
    biblioteka.dodaj_ksiazke(ksiazka_2)

    biblioteka.wypozycz_ksiazke("Lalka")

    dostepne = biblioteka.dostepne_ksiazki()

    assert len(dostepne) == 1
    assert dostepne[0].tytul == "Dziady"