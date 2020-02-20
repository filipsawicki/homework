from Meal.base.meal import Meal, get_sum_calories, get_print_list

p1 = Meal()
p1.set_posilek("Spaghetty", 220)

p2 = Meal()
p2.set_posilek("Steak", 80)

p3 = Meal()
p3.set_posilek("Paczek", 290)

Meal.get_posilek(p1)
Meal.get_posilek(p2)
Meal.get_posilek(p3)



del p2

get_sum_calories()

get_print_list()



