"""
List Less Than Ten
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_5(a: list):
    c = []
    for element in a:
        if element < 5:
            c.append(element)
    return print(c)


less_5(a)



b = [i for i in a if i < 5]
print(b)




