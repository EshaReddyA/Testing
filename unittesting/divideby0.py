import unittest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class TestDivide(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)

    def test_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_float_result(self):
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(1, 4), 0.25)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
