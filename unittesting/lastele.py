import unittest

def last_element(lst):
    try:
        return lst[-1]
    except IndexError:
        raise ValueError("List is empty")

class TestLastElement(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(last_element([1, 2, 3, 4]), 4)
        self.assertEqual(last_element(["a", "b", "c"]), "c")
        self.assertEqual(last_element([True, False, True]), True)

    def test_single_element_list(self):
        self.assertEqual(last_element([42]), 42)
        self.assertEqual(last_element(["hello"]), "hello")

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            last_element([])

if __name__ == '__main__':
    unittest.main()
