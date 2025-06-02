import unittest

def max_of_three(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c

class TestMaxOfThree(unittest.TestCase):

    def test_all_positive(self):
        self.assertEqual(max_of_three(1, 5, 3), 5)
        self.assertEqual(max_of_three(10, 20, 15), 20)

    def test_all_negative(self):
        self.assertEqual(max_of_three(-1, -5, -3), -1)
        self.assertEqual(max_of_three(-10, -20, -15), -10)


# Run tests
if __name__ == '__main__':
    unittest.main()
