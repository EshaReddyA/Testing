import unittest

def merge_lists(list1, list2):
    return list1 + list2

class TestMergeLists(unittest.TestCase):

    def test_regular_lists(self):
        self.assertEqual(merge_lists([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_lists(["a", "b"], ["c", "d"]), ["a", "b", "c", "d"])

    def test_empty_first_list(self):
        self.assertEqual(merge_lists([], [1, 2, 3]), [1, 2, 3])

    def test_empty_second_list(self):
        self.assertEqual(merge_lists([1, 2, 3], []), [1, 2, 3])

    def test_both_empty(self):
        self.assertEqual(merge_lists([], []), [])

    def test_with_duplicates(self):
        self.assertEqual(merge_lists([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])

if __name__ == '__main__':
    unittest.main()
