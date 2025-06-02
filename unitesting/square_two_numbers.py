import unittest

def square(n):
    return n * n

class TestSquare(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(5), 25)
        self.assertEqual(square(10), 100)

    def test_negative_numbers(self):
        self.assertEqual(square(-2), 4)
        self.assertEqual(square(-5), 25)

    def test_zero(self):
        self.assertEqual(square(0), 0)

if __name__ == '__main__':
    unittest.main()
