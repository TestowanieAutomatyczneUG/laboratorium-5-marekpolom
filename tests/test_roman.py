import unittest
import src.roman

roman = src.roman.roman

class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_a_single_i(self):
        self.assertEqual(roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(roman(3), "III")