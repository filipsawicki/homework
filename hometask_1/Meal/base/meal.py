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

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delete__(self, instance):
        # print(f"Pozycja {self.posilek} {self.kalorie} zostala usunieta")
        Meal.sum_cal -= self.kalorie
        del (self.posilek, self.kalorie)

    # setter - dodajemy posilek oraz jego kalorie,
    def set_posilek(self, posilek, kalorie):
        self.posilek = posilek
        self.kalorie = kalorie
        Meal.sum_cal += kalorie

    def get_posilek(self):
        return print(f" Posilek:  {self.posilek} - Kalorie: {self.kalorie}")


def get_sum_calories():
    return print(f'Suma kalorii wszystkich posilkow {Meal.sum_cal}')

# def get_print_list():
#     return print(i for i in Meal.meal_list)
