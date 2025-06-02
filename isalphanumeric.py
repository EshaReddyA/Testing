import unittest

def is_alphanumeric(s):
    return s.isalnum()

class TestIsAlphanumeric(unittest.TestCase):

    def test_all_letters(self):
        self.assertTrue(is_alphanumeric("HelloWorld"))

    def test_all_numbers(self):
        self.assertTrue(is_alphanumeric("123456"))

    def test_letters_and_numbers(self):
        self.assertTrue(is_alphanumeric("Hello123"))

    def test_with_space(self):
        self.assertFalse(is_alphanumeric("Hello World"))

    def test_with_symbols(self):
        self.assertFalse(is_alphanumeric("Hello!"))

    def test_empty_string(self):
        self.assertFalse(is_alphanumeric(""))

if __name__ == '__main__':
    unittest.main()
