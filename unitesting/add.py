import unittest

def sum_of_two(a, b):
    return a + b

class TestSumOfTwo(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum_of_two(2, 3), 5)

    def test_negative_add(self):
        self.assertEqual(sum_of_two(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()
