import unittest

def element_exists(lst, element):
    for item in lst:
        if item == element:
            return True
    return False

class TestElementExists(unittest.TestCase):

    def test_element_present(self):
        self.assertTrue(element_exists([1, 2, 3, 4], 3))
        self.assertTrue(element_exists(["a", "b", "c"], "b"))
        self.assertTrue(element_exists([None, True, False], None))

    def test_element_not_present(self):
        self.assertFalse(element_exists([1, 2, 3], 5))
        self.assertFalse(element_exists(["x", "y"], "z"))
        self.assertFalse(element_exists([], "anything")) 

    def test_duplicates(self):
        self.assertTrue(element_exists([1, 2, 2, 3], 2))

if __name__ == '__main__':
    unittest.main()
