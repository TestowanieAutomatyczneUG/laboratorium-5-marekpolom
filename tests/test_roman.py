import unittest
import roman from src.roman

class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_a_single_i(self):
        self.assertEqual(roman(1), "I")