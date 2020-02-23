"""
    Napisz funkcje stwierdzajaca czy podana jako argument liczba
    jest liczba pierwsza czy nie. Liczba jest pierwsza, kiedy dzieli sie
    tylko przez siebie i przez 1. Jednym z algorytmow wyszukiwania liczb
    pierwszych jest sprawdzenie czy zadna z liczb od 2 do LICZBA-1
    (lub od 2 do pierwiastek z LICZBA) nie dzieli badanej liczby bez reszty.
    Uwaga: 0 i 1 nie sa zaliczane ani do liczb pierwszych, ani do zlozonych.
"""


def is_prime_number(number):
    n = int(number)
    if n > 1 and (n / 1 == n) and (n % 2 != 0):
        return True
    elif n == 2:
        return True
    else:
        return False


