import unittest

def sum_list(lst):
    return sum(lst)

class TestSumList(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(sum_list([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_list([1, -2, 3, -4, 5]), 3)

    def test_empty_list(self):
        self.assertEqual(sum_list([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_list([42]), 42)

    def test_zeros(self):
        self.assertEqual(sum_list([0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()

