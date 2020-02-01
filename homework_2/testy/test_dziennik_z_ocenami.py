import unittest
from ..dziennik_z_ocenami import *


class TestOfAllGrades(unittest.TestCase):

    def test_of_all_grades(self):
        la = list_of_all_grades()
        self.assertEqual(la, ([4.0, 3.5, 4.0, 4.0, 4.5, 2.0, 2.0, 3.0, 5.0, 4.0, 3.0]))

class TestMaxGrade(unittest.TestCase):

    def test_max_grade(self):
        mg = highest_grade_from_list()
        self.assertEqual(mg, 5.0)



    def test_of_number_failed(self):
        nf = number_of_failed()
        self.assertEqual(nf, 2)
