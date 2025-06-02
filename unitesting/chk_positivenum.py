import unittest

def is_positive(n):
    return n > 0

class TestIsPositive(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_positive(1))
        self.assertTrue(is_positive(10))
        self.assertTrue(is_positive(0.5))

    def test_zero(self):
        self.assertFalse(is_positive(0))

    def test_negative_numbers(self):
        self.assertFalse(is_positive(-1))
        self.assertFalse(is_positive(-0.5))

if __name__ == '__main__':
    unittest.main()
