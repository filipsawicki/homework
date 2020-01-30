"""
    Napisz funkcje laczaca ze soba dwa napisy w sposob:
    najpierw pierwsza litera pierwszego napisu, potem pierwsza litera
    drugiego, druga litera drugiego napisu, itd...
    Funkcja powinna zwrocic nowy napis bedacy polaczeniem tych podanych
    jako parametry. Uwaga: wejsciowe napisy nie musza byc tej samej
    dlugosci!
    Przyklad:
    >> merge_strings("pies", "buda")
    pbiuedsa
    >> merge_strings("stop", "supermarket)
    sstuoopermarket
    W przypadku kiedy jakis napis jest dluzszy, nalezy go po prostu
    przepisac, podobnie jak to zostalo pokazane na drugim przykladzie.
    Laczy naprzemiennie napisy string1 oraz string2.

    :param string1: pierwszy napis do polaczenia.
    :param string2: drugi napis do polaczenia.
    :return: napis zlozony z podanych jako argumenty.
"""


def merge_strings(string1, string2):

    if len(string1) > len(string2):
        n = len(string1) - len(string2)
        return str("".join([a for b in zip(string1, string2) for a in b]) + string1[-n::])

    elif len(string2) > len(string1):
        n = len(string2) - len(string1)
        return str("".join([a for b in zip(string1, string2) for a in b]) + string2[-n::])

    else:
        return str("".join([a for b in zip(string1, string2) for a in b]))