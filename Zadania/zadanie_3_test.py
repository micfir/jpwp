import pytest

from zadanie_3 import SalaKinowa


@pytest.fixture
def sala():
    return SalaKinowa(10)


def test_utworzenie_sali(sala):
    assert sala.liczba_miejsc == 10
    assert sala.liczba_wolnych_miejsc() == 10


def test_nie_mozna_utworzyc_sali_z_zerowa_liczba_miejsc():
    with pytest.raises(ValueError):
        SalaKinowa(0)


def test_rezerwacja_miejsca(sala):
    sala.zarezerwuj_miejsce(3)

    assert sala.czy_miejsce_wolne(3) is False
    assert sala.liczba_wolnych_miejsc() == 9


def test_anulowanie_rezerwacji(sala):
    sala.zarezerwuj_miejsce(3)
    sala.anuluj_rezerwacje(3)

    assert sala.czy_miejsce_wolne(3) is True
    assert sala.liczba_wolnych_miejsc() == 10


def test_nie_mozna_zarezerwowac_tego_samego_miejsca_dwa_razy(sala):
    sala.zarezerwuj_miejsce(5)

    with pytest.raises(ValueError):
        sala.zarezerwuj_miejsce(5)


def test_nie_mozna_anulowac_niezarezerwowanego_miejsca(sala):
    with pytest.raises(ValueError):
        sala.anuluj_rezerwacje(4)


@pytest.mark.parametrize("numer_miejsca", [0, -1, 11])
def test_nieprawidlowy_numer_miejsca_zglasza_blad(sala, numer_miejsca):
    with pytest.raises(ValueError):
        sala.zarezerwuj_miejsce(numer_miejsca)


def test_liczba_wolnych_miejsc_po_kilku_rezerwacjach(sala):
    sala.zarezerwuj_miejsce(1)
    sala.zarezerwuj_miejsce(2)
    sala.zarezerwuj_miejsce(3)

    assert sala.liczba_wolnych_miejsc() == 7