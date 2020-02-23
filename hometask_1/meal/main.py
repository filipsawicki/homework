from hometask_1.meal.baza.meal import Meal, get_sum_calories, get_dict

spaghetty = Meal()
spaghetty.set_posilek("Spaghetty", 220)

steak = Meal()
steak.set_posilek("Steak", 80)

eaggs = Meal()
eaggs.set_posilek("Eaggs", 50)

get_sum_calories()


Meal.delete_meal(steak)

get_sum_calories()

spaghetty.get_posilek()

get_dict()