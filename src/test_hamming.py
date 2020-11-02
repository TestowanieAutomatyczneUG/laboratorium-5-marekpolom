import unittest
import hamming

class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        self.assertEqual(hamming.distance("", ""), 0)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")