import unittest

def sub(a, b):
    return a - b

class Testsub(unittest.TestCase):

    def test_sub_pos_numbers(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(40, 20), 20)

    def test_sub_neg_numbers(self):
        self.assertEqual(sub(-2, -3), 1)
        self.assertEqual(sub(-5, 5), -10)

if __name__ == '__main__':
    unittest.main()
