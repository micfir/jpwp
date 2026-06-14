class KontoBankowe:
    """
    Prosta klasa reprezentująca konto bankowe.
    """

    def __init__(self, wlasciciel, saldo=0):
        # TODO 1: Zainicjalizuj atrybuty. Dodaj walidację: saldo nie może być ujemne.

    def wplata(self, kwota):
        # TODO 2: Dodaj walidację: kwota wpłaty musi być dodatnia. Saldo musi się zwiekszyć po wpłacie.

    def wyplata(self, kwota):
        # TODO 3: Dodaj walidację: kwota wypłaty musi być dodatnia. Saldo musi się zwiekszyć po wypłacie. Nie można wypłacić pieniędzy których nie ma na koncie.

    def przelew(self, inne_konto, kwota):
        # TODO 4: Zrealizuj przelew na `inne_konto` przy użyciu dostępnych metod.