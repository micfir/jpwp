class Koszyk:
    """Prosta klasa reprezentująca koszyk zakupowy."""

    def __init__(self):
        self.produkty = {}

    def dodaj_produkt(self, nazwa, cena, ilosc=1):
        """
        Dodaje produkt do koszyka.

        Jeśli produkt już istnieje, zwiększa jego ilość.
        """

        # TODO 1: Cena oraz ilość muszą być w poprawnym zakresie.

        # TODO 2: jeśli produktu nie ma w koszyku, dodaj go z ceną i ilością 0.

        # TODO 3: Zwiększ ilość produktu o podaną ilość.


    def usun_produkt(self, nazwa):
        """
        Usuwa produkt z koszyka.
        """

        # TODO 4: Co jeśli produktu nie ma w koszyku?

        del self.produkty[nazwa]


    def oblicz_sume(self):
        """
        Oblicza łączną wartość koszyka.
        """

        # TODO 4: Zwróć sumę: cena razy ilość dla każdego produktu.


    def oblicz_sume_po_rabacie(self, rabat):
        """
        Oblicza wartość koszyka po rabacie.

        Rabat podajemy jako liczbę od 0 do 1.
        Przykład: 0.10 oznacza 10%.
        """

        # TODO 5: Rabat musi być w poprawnym zakresie.

        return self.oblicz_sume() * (1 - rabat)