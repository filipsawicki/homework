import pytest
from ..my_filter import my_filter


def test_01_my_filter():
    print("Test 01")
    ltest = [-3, -2, -1, 0, 1, 2, 3]
    assert my_filter(callable, ltest) == [1, 2, 3]


def test_02_my_filter():
    print("Test 02")
    ltest = [-4, -6, -9, 0, 1, 2, 3]
    assert my_filter(callable, ltest) == [1, 2, 3]


def test_03_my_filter():
    print("Test 03")
    ltest = [-3, -2, -1, 0, 2, 2, 3]
    assert my_filter(callable, ltest) != [1, 2, 3]


def test_04_my_filter():
    print("Test 04")
    ltest = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert my_filter(callable, ltest) == [1, 2, 3, 4, 5]
