import pytest

from zadanie_2 import wczytaj_oceny


def zapisz_csv(tmp_path, tresc):
    plik = tmp_path / "oceny.csv"
    plik.write_text(tresc, encoding="utf-8")
    return plik


def test_poprawne_wczytanie_pliku(tmp_path):
    plik = zapisz_csv(
        tmp_path,
        "imie,punkty,max_punktow\nAnna,80,100\nJan,45,100\nOla,30,50\n",
    )

    wynik = wczytaj_oceny(plik)

    assert len(wynik) == 3
    assert wynik[0] == {
        "imie": "Anna",
        "punkty": 80.0,
        "max_punktow": 100.0,
        "procent": 80.0,
        "zaliczyl": True,
    }
    assert wynik[1]["zaliczyl"] is False
    assert wynik[2]["procent"] == 60.0


def test_ignoruje_puste_linie(tmp_path):
    plik = zapisz_csv(
        tmp_path,
        "imie,punkty,max_punktow\nAnna,80,100\n\nJan,50,100\n",
    )

    wynik = wczytaj_oceny(plik)

    assert len(wynik) == 2


def test_pusty_plik_zwraca_pusta_liste(tmp_path):
    plik = zapisz_csv(tmp_path, "")

    assert wczytaj_oceny(plik) == []


def test_brak_pliku_zglasza_file_not_found(tmp_path):
    nieistniejacy_plik = tmp_path / "brak.csv"

    with pytest.raises(FileNotFoundError):
        wczytaj_oceny(nieistniejacy_plik)


def test_punkty_wieksze_niz_max_zglaszaja_blad(tmp_path):
    plik = zapisz_csv(tmp_path, "imie,punkty,max_punktow\nAnna,120,100\n")

    with pytest.raises(ValueError):
        wczytaj_oceny(plik)


def test_ujemne_punkty_zglaszaja_blad(tmp_path):
    plik = zapisz_csv(tmp_path, "imie,punkty,max_punktow\nAnna,-5,100\n")

    with pytest.raises(ValueError):
        wczytaj_oceny(plik)


def test_bledna_wartosc_liczbowa_zglasza_blad(tmp_path):
    plik = zapisz_csv(tmp_path, "imie,punkty,max_punktow\nAnna,abc,100\n")

    with pytest.raises(ValueError):
        wczytaj_oceny(plik)