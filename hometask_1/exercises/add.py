"""
add from morsels
"""

matrix1 = [[1, -2], [-3, 4]]

matrix2 = [[2, -1], [0, -1]]


def add(a: list, b: list) -> list:
    """Function adding two list  """
    temp = zip(a, b)
    print(list(temp))





print(add(matrix1, matrix2))
