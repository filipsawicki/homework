"""
    Stworz prosty symulator gry karcianej wojna.
    Zadaniem Twojej funkcji jest wskazanie, ktora karta
    zwyciezy. Parametrami sa znaki card1 oraz card2.
    Moga one przyjmowac wartosci:
    <"1", "2", "3", ..., "10", "J", "D", "K", "A"> - wielkosc
    liter bedzie miala znaczenie (choc mozna przedstawic rozwiazanie,
    w ktorym nie bedzie znaczylo czy litera jest duza czy mala).
    Funkcja powinna zwracac liczbe 1, jezeli wygra gracz 1,
    2 - jezeli zwyciezy gracz 2 lub 0 jesli karty sa takie same.
    Przyklady:
    >> determine_the_winner("5", "2")
    1
    >> determine_the_winner("D", "A")
    2
    >> determine_the_winner("K", "8")
    1
    >> determine_the_winner("4", "4")
    0
    Wskazuje zwyciezce potyczki w grze wojna.
    :param card1: litera (string) reprezentujaca karte gracza 1.
    :param card2: litera (string) reprezentujaca karte gracza 2.
    :return: 0 dla remisu, 1 jesli zwyciezy gracz 1, 2 dla zwyciestwa gracza 2.
"""



def determine_the_winner(card1, card2):
    cards_dict = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'D': 11, 'K': 12,
                  'A': 13}


    if card1 > card2:
        return 1
    elif card2 > card1:
        return 2
    return 0



#print(determine_the_winner('A', 'D'))
