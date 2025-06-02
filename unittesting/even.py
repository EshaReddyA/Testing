import unittest

def is_even(n):
    return n % 2 == 0

class TestIsEven(unittest.TestCase):

    def test_even_numbers(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(10))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))

    def test_odd_numbers(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-3))

if __name__ == '__main__':
    unittest.main()
