import csv


def wczytaj_oceny(sciezka):
    """
    Wczytuje oceny studentów z pliku CSV.

    Plik CSV powinien mieć kolumny:
    imie,punkty,max_punktow

    Funkcja zwraca listę słowników z informacjami:
    imie, punkty, max_punktow, procent, zaliczyl.
    """

    wyniki = []

    with open(sciezka, encoding="utf-8", newline="") as plik:
        czytnik = csv.DictReader(plik)

        for wiersz in czytnik:
            if not wiersz or not wiersz.get("imie"):
                continue

            try:
                # TODO 1: Zamień wartość z kolumny "punkty" na float.

                # TODO 2: Zamień wartość z kolumny "max_punktow" na float.

            except ValueError as blad:
                raise ValueError("Niepoprawna wartość liczbowa") from blad

            # TODO 3: Co jeśli punkty są ujemne lub wieksze od makymalnych?

            # TODO 4: Oblicz procent zdobytych punktów.

            wyniki.append({
                "imie": wiersz["imie"],
                "punkty": punkty,
                "max_punktow": max_punktow,
                "procent": procent,
                # TODO 5: sprawdź, czy student zaliczył na minimum 50%.
            })

    return wyniki