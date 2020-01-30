"""
    Napisz funkcje przyjmujaca dwa zbiory (sety) jako parametry
    i znajdujaca liczby, ktore znajduja sie zarowno w jednym zbiorze,
    jak i w drugim.
    Funkcja powinna zwrocic set powtarzajacych sie liczb. Jezeli zadna
    liczba sie nie powtarza, funkcja powinna zwrocic pusty zbior.
    Uwaga: w Pythonie pusty set (zbior) deklaruje sie tak:
    >> pusty = set()
    a nie tak:
    >> pusty = {} # w taki sposob deklaruje sie slownik.
    Zadanie powinno zostac wykonane w inny sposob niz za pomoca
    uzycia skladni:
    >> set1 & set2
    ktore w skrocie ustala czesc wspolna obu zbiorow.
    Znajduje wspolne liczby z odbydwoch zbiorow.
    :param set1: pierwszy zbior liczbowy.
    :param set2: drugi zbior liczbowy.
    :return: nowy set posiadajacy liczby, ktore wchodza w sklad zarowno
        zbioru set1 jak i zbioru set2.
"""


def find_common_numbers(set1, set2):
    set3 = set()
    set4 = set()
    if len(set2.intersection(set1)) > 0:
        return set1.intersection(set2)
    else:
        return set3






# set1 = {1, 2, 3, 4}
# # set2 = {2, 3, 5, 7, 9, 10}
#
# set1 = {1, 2, 3, 4}
# set2 = {5, 6, 7, 8}
#
#
# print(find_common_numbers(set1, set2))
