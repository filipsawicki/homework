"""
add from morsels
"""

matrix1 = [[1, -2], [-3, 4]]

matrix2 = [[2, -1], [0, -1]]


def add(a: list, b: list) -> list:
    """Function adding two list  """
    return [a[i] + b[i] for i in range(len(a))]



print(add(matrix1, matrix2))
