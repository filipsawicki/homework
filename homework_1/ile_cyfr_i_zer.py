"""
    Napisz dwie niezalezne funkcje rozwiazujace nastepujace problemy:
    a) count_digits powinno zliczac ilosc cyfr w liczbie calkowitej,
       ktora zostanie podana jako argument,
    b) count_zeros powinno zliczac ilosc zer w liczbie calkowitej, ktora zostanie
       podana jako argument.
    Przyklady:
    >> x = count_digits(1234)
    >> print(x)
    4
    >> x = count_zeros(1000)
    >> print(x)
    3
    Zadania mozna rozwiazac w sposob "matematyczny", ale rowniez
    wykorzystujac uproszczenia Pythona.
    Podpowiedz: a gdyby tak liczbe rzutowac na napis?
"""

number = 1234567891011000

def count_digits(number):
    return len(str(number))



def count_zeros(number):
    numbers = [int(i) for i in str(number)]
    num_zeros = 0
    for i in numbers:
        if i == 0:
            num_zeros += 1
    return num_zeros


