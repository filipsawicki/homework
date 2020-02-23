"""
meal class , zabawa klasami
"""


class Meal:
    sum_cal = 0
    meal_dict = {}

    # knstruktor
    def __init__(self, posilek=None, kalorie=None):
        self.posilek = posilek
        self.kalorie = kalorie

    # metoda usuwa posilek zmniejszajac liczbe wszystkich kalorii
    def delete_meal(self):
        print(f"Posiłek : {self.posilek} - {self.kalorie} kalorii -- zostal usuniety!")
        Meal.sum_cal -= self.kalorie
        del (self.posilek, self.kalorie)

    # metoda setter - dodajemy posilek oraz jego kalorie,
    def set_posilek(self, posilek, kalorie):
        self.posilek = posilek
        self.kalorie = kalorie
        Meal.sum_cal += kalorie
        Meal.meal_dict.update({self.posilek: self.kalorie})

    # metoda getter - wyswietla posilek oraz jego kalorie
    def get_posilek(self):
        return print(f"Posilek:  {self.posilek} - Kalorie: {self.kalorie}")





    # funkcja wyswietla sume wszystkich kalorii
def get_sum_calories():
    return print(f' Suma kalorii wszystkich posilkow {Meal.sum_cal}')

    # funkcja wyswietla slownik ze wszystkimi posilkami
def get_dict():
    return print(f' Słownik wszystkich posilkow {Meal.meal_dict}')
