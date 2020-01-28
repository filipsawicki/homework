"""
    Napisz funkcje sprawdzajaca czy napis podany jako argument do niej
    jest palindromem. Palindrom to napis, ktory czytany od lewej
    do prawej brzmi tak samo jak czytany od prawej do lewej, np kajak.
    Dla ulatwienia zaloz, ze napis bedzie zawsze jednym slowem.
    Zakladamy, ze pusty string jest palindromem.
    Sprawdza czy podany string (jedno slowo) jest palindromem.

    :param string: napis do sprawdzenia.
    :return: True jezeli napis jest palindromem,
             False w przeciwnym wypadku.
"""


def check_if_palindrome(string):

    lstr = [string]
    revlstr = reversed(lstr)
    for i in lstr:
        if i in revlstr:
            return True
    else:
        return False
    #return string == string[::-1] - drugie rozwiazanie


