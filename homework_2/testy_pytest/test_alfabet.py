import pytestfrom ..alfabet import get_alphabet_signs

def test_01():
    assert get_alphabet_signs(5) == ["A", "B", "C", "D", "E"]
    assert get_alphabet_signs(4) == ["A", "B", "C", "D"]
    assert get_alphabet_signs(2) == ["A", "B"]


def test_02():
    assert get_alphabet_signs(9) != ["A", "B", "C", "D", "E"]