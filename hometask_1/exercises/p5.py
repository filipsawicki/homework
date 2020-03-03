"""
List Overlap
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def overlap(a, b):
    c = []
    for i in b:
        c.append(i)
    for x in a:
        if x not in c:
            c.append(x)
    return c


print(overlap(a, b))

def inter(a, b):
    c = list(set(a+b))
    return c

print(inter(a, b))
