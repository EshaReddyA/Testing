import unittest

def str_length(s):
    return len(s)

class TestStringLength(unittest.TestCase):

    def test_regular_str(self):
        self.assertEqual(str_length("hello"), 5)
        self.assertEqual(str_length("world"), 5)
        self.assertEqual(str_length("python"), 6)

    def test_empty_str(self):
        self.assertEqual(str_length(""), 0)

    def test_spaces(self):
        self.assertEqual(str_length(" "), 1)
        self.assertEqual(str_length("   "), 3)

    def test_special_characters(self):
        self.assertEqual(str_length("@#es"), 4)

if __name__ == '__main__':
    unittest.main()
