import pytest

from zadanie_4 import Koszyk


@pytest.fixture
def koszyk():
    return Koszyk()


def test_pusty_koszyk_ma_sume_zero(koszyk):
    assert koszyk.oblicz_sume() == 0


def test_dodanie_jednego_produktu(koszyk):
    koszyk.dodaj_produkt("Laptop", 3000, 1)

    assert "Laptop" in koszyk.produkty
    assert koszyk.produkty["Laptop"]["cena"] == 3000
    assert koszyk.produkty["Laptop"]["ilosc"] == 1


def test_dodanie_kilku_produktow(koszyk):
    koszyk.dodaj_produkt("Laptop", 3000, 1)
    koszyk.dodaj_produkt("Myszka", 100, 2)

    assert len(koszyk.produkty) == 2
    assert koszyk.oblicz_sume() == 3200


def test_dodanie_tego_samego_produktu_zwieksza_ilosc(koszyk):
    koszyk.dodaj_produkt("Myszka", 100, 2)
    koszyk.dodaj_produkt("Myszka", 100, 3)

    assert koszyk.produkty["Myszka"]["ilosc"] == 5
    assert koszyk.oblicz_sume() == 500


def test_usuniecie_produktu(koszyk):
    koszyk.dodaj_produkt("Laptop", 3000, 1)
    koszyk.usun_produkt("Laptop")

    assert "Laptop" not in koszyk.produkty
    assert koszyk.oblicz_sume() == 0


def test_nie_mozna_usunac_nieistniejacego_produktu(koszyk):
    with pytest.raises(ValueError):
        koszyk.usun_produkt("Telefon")


def test_obliczenie_sumy_koszyka(koszyk):
    koszyk.dodaj_produkt("Laptop", 3000, 1)
    koszyk.dodaj_produkt("Myszka", 100, 2)
    koszyk.dodaj_produkt("Klawiatura", 200, 1)

    assert koszyk.oblicz_sume() == 3400
def test_obliczenie_sumy_po_rabacie(koszyk):
    koszyk.dodaj_produkt("Laptop", 3000, 1)

    assert koszyk.oblicz_sume_po_rabacie(0.10) == pytest.approx(2700)


def test_rabat_zero_nie_zmienia_sumy(koszyk):
    koszyk.dodaj_produkt("Laptop", 3000, 1)

    assert koszyk.oblicz_sume_po_rabacie(0) == 3000


def test_rabat_100_procent_daje_zero(koszyk):
    koszyk.dodaj_produkt("Laptop", 3000, 1)

    assert koszyk.oblicz_sume_po_rabacie(1) == 0


def test_nie_mozna_dodac_produktu_z_ujemna_cena(koszyk):
    with pytest.raises(ValueError):
        koszyk.dodaj_produkt("Laptop", -3000, 1)


def test_nie_mozna_dodac_produktu_z_zerowa_iloscia(koszyk):
    with pytest.raises(ValueError):
        koszyk.dodaj_produkt("Laptop", 3000, 0)


@pytest.mark.parametrize("rabat", [-0.1, 1.5])
def test_niepoprawny_rabat_zglasza_blad(koszyk, rabat):
    koszyk.dodaj_produkt("Laptop", 3000, 1)

    with pytest.raises(ValueError):
        koszyk.oblicz_sume_po_rabacie(rabat)