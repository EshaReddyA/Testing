import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, 5), 0)

if __name__ == '__main__':
    unittest.main()
