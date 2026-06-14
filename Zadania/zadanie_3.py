class SalaKinowa:
    """
    Prosta klasa reprezentująca salę kinową.
    """

    def __init__(self, liczba_miejsc):
        if liczba_miejsc <= 0:
            raise ValueError("Liczba miejsc musi być większa od zera")

        self.liczba_miejsc = liczba_miejsc

        # TODO 1: utwórz pusty zbiór na zarezerwowane miejsca.


    def _sprawdz_numer_miejsca(self, numer_miejsca):
        """
        Sprawdza, czy numer miejsca mieści się w zakresie sali.
        Miejsca są numerowane od 1 do liczba_miejsc.
        """
        # TODO 2


    def zarezerwuj_miejsce(self, numer_miejsca):
        """
        Rezerwuje wybrane miejsce w sali kinowej.
        """

        self._sprawdz_numer_miejsca(numer_miejsca)

        # TODO 3: Nie można zarezerwować zajętego już miejsca. 

        # TODO 4: Dodaj numer miejsca do zbioru zarezerwowanych miejsc.


    def anuluj_rezerwacje(self, numer_miejsca):
        """
        Anuluje rezerwację wybranego miejsca.
        """

        self._sprawdz_numer_miejsca(numer_miejsca)

        # TODO 5: Żeby anulować trzeba taka rezerwacje posiadać.

        # TODO 6: Usuń numer miejsca ze zbioru zarezerwowanych miejsc.


    def czy_miejsce_wolne(self, numer_miejsca):
        """
        Zwraca True, jeśli miejsce jest wolne.
        Zwraca False, jeśli miejsce jest zarezerwowane.
        """

        self._sprawdz_numer_miejsca(numer_miejsca)

        # TODO 7: Zwróć True, jeśli miejsce nie jest zarezerwowane.


    def liczba_wolnych_miejsc(self):
        """
        Zwraca liczbę wolnych miejsc w sali.
        """

        # TODO 8: Zwróć liczbę wolnych miejsc.