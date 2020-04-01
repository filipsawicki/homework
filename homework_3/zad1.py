"""
    Zadanie bedzie polegalo na analizie pliku male_oscars.csv.
    Wczytaj plik csv i wykonaj ponizsze zadania:
    a) napisz funkcje, ktora zwroci imie i nazwisko najstarszego zdobywcy oskara z tej listy (kolumna year),
    b) napisz funkcje, ktora posortuje zdobywcow oskara od najstarszego do najmlodszego,
    c) napisz funkcje, ktora doda nowy wiersz do pliku: powinna ona przyjmowac tylko rok, imie i nazwisko zwyciezcy
    oraz tytul filmu - indeks powinien byc ustalany automatycznie.
    Zabezpiecz program na wypadek gdyby argument filename byl sciezka do nieistniejacego pliku. Użyj bloków
    try-except w każdej funkcji.
"""
import csv

age_column = 3
name_column = 4


def get_name_of_the_oldest_winner(filename: str) -> str:
    """Wyciaga imie i nazwisko najstarszego zwyciezcy oskarow.
    :param filename: sciazka do pliku.
    :return: imie i nazwisko najstarszego zwyciezcy jako string
    """
    try:
        with open(filename) as csvfile:
            first = csv.reader(csvfile, delimiter=',')
            oldest_person = None
            oldest_person_age = 0

            for i, row in enumerate(first):
                if i == 0:
                    continue

                years_old = int(row[age_column - 1].strip())
                if years_old > oldest_person_age:
                    oldest_person_age = years_old
                    name = row[name_column - 1].strip(' "')
                    oldest_person = name

            return oldest_person
    except FileNotFoundError:
        print(f"File {filename} doesn't exist!")


def sort_oscar_winners_due_to_age(filename: str) -> list:
    """Sortuje liste zwyciezcow wedlug ich wieku - od najstarszego do najmlodszego.
    :param filename: sciazka do pliku.
    :return: posortowana lista.
    """
    not_sorted_column = ' "Age"'
    try:
        with open(filename) as csvfile:
            second = csv.DictReader(csvfile)
            person_list = []

            for row in second:
                person_list.append(row)

                person_list.sort(key=lambda x: int(x[not_sorted_column].strip()), reverse=True)
        return person_list
    except FileNotFoundError:
        print(f"File {filename} doesn't exist!")


def add_new_winner(filename: str):
    """Dodaje nowy wiersz do pliku .csv.
    :param filename: sciazka do pliku.
    """
    try:
        with open(filename, "r+", newline="") as csv_file:

            my_reader = csv.DictReader(csv_file)

            winners = []
            for row in my_reader:
                winners.append(row)

            last_index = len(winners)
            # Przyklad pobrania danych, mozna to zrobic rowniez poprzez argumenty
            year = " " + input("Year: ")
            age = " " + input("Age: ")
            name = f' "{input("Name: ")}"'
            movie = f' "{input("Movie: ")}"'

            my_writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_MINIMAL, quotechar="'")
            my_writer.writerow([int(last_index) + 1, year, age, name, movie])
    except FileNotFoundError:
        print(f"File  {filename} doesn't exist!")


