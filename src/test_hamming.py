import unittest
import hamming

class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        self.assertEqual(hamming.distance("", ""), 0)

    def test_single_letter_identical_strands(self):
        self.assertEqual(hamming.distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(hamming.distance("G", "T"), 1)

    def test_long_identical_strands(self):
        self.assertEqual(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")