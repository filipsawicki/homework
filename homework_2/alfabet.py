"""
    Napisz funkcje, ktora poprosi o liczbe, a w zamian zwroci liste
    z tyloma pierwszymi literami alfabetu.
    Pomocna bedzie tutaj tablica ascii oraz wbudowane funkcje ord() oraz chr().
    Przyklad:
    >> x = get_alphabet_signs(5)
    >> print(x)
    ["A", "B", "C", "D", "E"]
    Ustala <signs_amount> pierwszych liczb alfabetu.

    :param sings_amount: liczba naturalna <0; 26>.
    :returns: lista stringow duzych liter, ich ilosc zalezy od parametru signs_amount.
"""


def get_alphabet_signs(sings_amount):

    n = sings_amount
    alphabet = [chr(i) for i in range(65, 91)]
    return alphabet[:n]

print(get_alphabet_signs(5))