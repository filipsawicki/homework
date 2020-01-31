import unittest
from homework_2.alfabet import get_alphabet_signs


class TestAlfabetSign(unittest.TestCase):

    def test_1_alphabet_case(self):
        a = get_alphabet_signs(5)
        self.assertTrue(a, ["A", "B", "C", "D", "E"])

    def test_2_alphabet_case(self):

        self.assertEqual(get_alphabet_signs(4), ["A", "B", "C", "D"])

    def test_3_alphabet_case(self):

        self.assertEqual(get_alphabet_signs(2), ["A", "B"])

    def test_4_alphabet_case(self):

        self.assertIsNot(get_alphabet_signs(9), ["A", "B", "C", "D", "E"])




if __name__ == '__main__':
    unittest.main()