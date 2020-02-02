"""
    Dla podanego slownika reprezentujacego oceny, napisz 4 funkcje:
    a) pierwsza powinna zwracac liste wszystkich ocen ze slownika,
    b) druga powinna ustalic i zwrocic maksymalna ocene z dziennika,
    c) trzecia ustala ile osob nie zaliczylo przedmiotu (kazda osoba z ocena 2.0),
    d) czwarta powinna zwrocic imie osoby z najwyzsza ocena.
    Przykladowy "dziennik" reprezentuje slownik CLASS_REGISTER.
    Nazwy i parametry funkcji do wlasnego wyboru :)
"""

CLASS_REGISTER = {
    "Ania": 4.0,
    "Jakub": 3.5,
    "Roman": 4.0,
    "Kasia": 4.0,
    "Aneta": 4.5,
    "Wojtek": 2.0,
    "Ola": 2.0,
    "Monika": 3.0,
    "Ula": 5.0,
    "Mikolaj": 4.0,
    "Robert": 3.0
}


def list_of_all_grades():

    return list(CLASS_REGISTER.values())


def highest_grade_from_list():

    return max(list(CLASS_REGISTER.values()))


def number_of_failed():

    clas_list = (CLASS_REGISTER.values())
    ming = min(list(CLASS_REGISTER.values()))
    num_min = 0
    for i in clas_list:
        if i == ming:
            num_min += 1
    return num_min


def name_of_highest_grade():

    keys = list(CLASS_REGISTER.keys())
    values = list(CLASS_REGISTER.values())
    return keys[values.index(max(values))]

