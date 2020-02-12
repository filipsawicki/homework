from homework_2.my_map import my_map


def test_01_my_map():
    print("test 01")
    list_test = [-3, -2, -1, 0, 1, 2, 3]
    assert my_map(lambda x: x+1, list_test) == [-2, -1, 1, 2, 3, 4]

def test_02_my_map():
    print("test 02")
    list_test = [-3, -2, 1]
    assert my_map(lambda x: x+2, list_test) == [-1, 0, 3]


def test_03_my_map():
    print("test 03")
    list_test = [-3, -2, -1, 0, 1, 2, 3]
    assert my_map(lambda x: x*2, list_test) == [-2, -1, 1, 2, 3, 4]