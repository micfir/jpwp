import pytest

from zadanie_1 import KontoBankowe


def test_utworzenie_konta():
    konto = KontoBankowe("Anna", 100)
    assert konto.wlasciciel == "Anna"
    assert konto.saldo == 100


def test_nie_mozna_utworzyc_konta_z_ujemnym_saldem():
    with pytest.raises(ValueError):
        KontoBankowe("Anna", -100)


def test_wplata_zwieksza_saldo():
    konto = KontoBankowe("Anna", 100)
    konto.wplata(50)
    assert konto.saldo == 150


@pytest.mark.parametrize("kwota", [0, -10])
def test_wplata_kwoty_niedodatniej_zglasza_blad(kwota):
    konto = KontoBankowe("Anna", 100)
    with pytest.raises(ValueError):
        konto.wplata(kwota)


def test_wyplata_zmniejsza_saldo():
    konto = KontoBankowe("Anna", 100)
    konto.wyplata(40)
    assert konto.saldo == 60


def test_nie_mozna_wyplacic_wiecej_niz_saldo():
    konto = KontoBankowe("Anna", 100)
    with pytest.raises(ValueError):
        konto.wyplata(150)


def test_przelew_miedzy_kontami():
    nadawca = KontoBankowe("Anna", 500)
    odbiorca = KontoBankowe("Jan", 100)

    nadawca.przelew(odbiorca, 200)

    assert nadawca.saldo == 300
    assert odbiorca.saldo == 300


def test_przelew_przy_braku_srodkow_zglasza_blad():
    nadawca = KontoBankowe("Anna", 100)
    odbiorca = KontoBankowe("Jan", 100)

    with pytest.raises(ValueError):
        nadawca.przelew(odbiorca, 150)

    assert nadawca.saldo == 100
    assert odbiorca.saldo == 100