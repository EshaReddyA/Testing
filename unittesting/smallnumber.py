import unittest

def min_of_three(a, b, c):
    if (a <= b) and (a <= c):
        return a
    elif (b <= a) and (b <= c):
        return b
    else:
        return c

class TestMinOfThree(unittest.TestCase):

    def test__positive(self):
        self.assertEqual(min_of_three(1, 5, 3), 1)
        self.assertEqual(min_of_three(10, 20, 15), 10)

    def test__negative(self):
        self.assertEqual(min_of_three(-1, -5, -3), -5)
        self.assertEqual(min_of_three(-10, -20, -15), -20)

if __name__ == '__main__':
    unittest.main()
