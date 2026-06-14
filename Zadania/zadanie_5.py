class Ksiazka:
    """
    Klasa reprezentująca książkę w bibliotece.
    """

    def __init__(self, tytul, autor):
        if not tytul:
            raise ValueError("Tytuł nie może być pusty")

        if not autor:
            raise ValueError("Autor nie może być pusty")

        # TODO 1: Zainicjalizuj atrybuty. Książka na początku nie jest wypożyczona.


class Biblioteka:
    """
    Klasa reprezentująca prosty system biblioteczny.
    """

    def __init__(self):
        self.ksiazki = []

    def dodaj_ksiazke(self, ksiazka):
        """
        Dodaje książkę do biblioteki.
        """

        self.ksiazki.append(ksiazka)

    def usun_ksiazke(self, tytul):
        """
        Usuwa książkę z biblioteki po tytule.
        """

        ksiazka = self.znajdz_ksiazke(tytul)

        # TODO 2: Usuń znalezioną (istniejącą!) książkę z listy książek.

    def znajdz_ksiazke(self, tytul):
        """
        Wyszukuje książkę po tytule.
        Wielkość liter nie ma znaczenia.
        """

        for ksiazka in self.ksiazki:
            # TODO 3: Sprawdź, czy tytuł książki zgadza się z podanym tytułem.

                # TODO 4: Jeśli tak, zwróć znalezioną książkę.
                
        return None
        

    def wypozycz_ksiazke(self, tytul):
        """
        Wypożycza książkę.
        """

        ksiazka = self.znajdz_ksiazke(tytul)

        if ksiazka is None:
            raise ValueError("Książka nie istnieje")

        # TODO 5: Jeśli książka jest już wypożyczona, zgłoś ValueError.
   
        # TODO 6: Ustaw książkę jako wypożyczoną.

    def zwroc_ksiazke(self, tytul):
        """
        Zwraca wypożyczoną książkę.
        """

        ksiazka = self.znajdz_ksiazke(tytul)

        if ksiazka is None:
            raise ValueError("Książka nie istnieje")

        # TODO 7: Jeśli książka nie była wypożyczona, zgłoś ValueError.

        # TODO 8: Ustaw książkę jako niewypożyczoną.

    def dostepne_ksiazki(self):
        """
        Zwraca listę książek, które nie są wypożyczone.
        """

        # TODO 9: Zwróć listę książek, które nie są wypożyczone.