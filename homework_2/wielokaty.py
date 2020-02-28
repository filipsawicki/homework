from abc import ABC, abstractmethod
from typing import Union


class Wielokat(ABC):

    @abstractmethod
    def oblicz_pole(self) -> Union[int, float]:  # Union sugeruje ze funkcja moze zwrocic inta albo floata
        pass

class Kwadrat(Wielokat):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self) -> Union[int, float]:
        return self.bok ** 2


class Prostokat(Wielokat):
    def __init__(self, bok1, bok2):
        self.bok1 = bok1
        self.bok2 = bok2

    def oblicz_pole(self) -> Union[int, float]:
        return self.bok1 * self.bok2


class Trojkat(Wielokat):
    def __init__(self, bok, wysokosc):
        self.bok = bok
        self.wysokosc = wysokosc

    def oblicz_pole(self) -> Union[int, float]:
        return 1 / 2 * self.bok * self.wysokosc


def licz_pola(wielokaty: list) -> list:
    list_area = []

    for elements in wielokaty:
        list_area.append((elements.oblicz_pole()))

    return list_area


