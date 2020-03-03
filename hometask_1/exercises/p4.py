"""
Divisors
"""

#num = int(input(f"choose a number from 1 to 100: "))

def division(num):
    x = range(2, num+1)
    lista_temp = []
    lista_dzielnikow = []
    for elements in x:
        if elements % 2 == 0:
            lista_temp.append(elements)
            print(lista_temp)
    for element in lista_temp:
        if num / element != 0:
            lista_dzielnikow.append(element)
        return lista_dzielnikow

print(division(25))

p5