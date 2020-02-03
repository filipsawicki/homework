"""
    Napisz funkcje symulujaca rzuty kostka szescioscienna.
    Parametr number_of_throws mowi, ile razy nalezy wykonac losowanie
    (czyli rzucenie koscia do gry). Funkcja zasymuluje gre, po czym
    powinna zwrocic najczesciej wylosowywana liczbe.
    Na potrzeby symulacji mozna wykorzystac modul random i jego funkcje
    randint. Zachecam do przejrzenia dokumentacji.
    Symuluje rzuty kostka i zwraca najczesciej pojawiajaca sie liczbe.
    :param number_of_throws: liczba rzutow kostka do wykonania.
    :returns: najczesciej pojawiajaca sie liczba (int; od 1 do 6)
"""
import random
from statistics import mode


def get_most_common_number(number_of_throws):

    number_of_throws = int(input(" Podaj liczbe rzutow "))
    dice_points = []
    while number_of_throws > 0:
        throw = random.randrange(1, 7)
        dice_points.append(throw)
        number_of_throws -= 1
    print(dice_points)
    return mode(dice_points)

print(get_most_common_number(1))