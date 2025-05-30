import unittest

def is_uppercase(s):
    return s.isupper()

class TestIsUppercase(unittest.TestCase):

    def test_all_uppercase(self):
        self.assertTrue(is_uppercase("HELLO"))

    def test_mixed_case(self):
        self.assertFalse(is_uppercase("Hello"))

    def test_all_lowercase(self):
        self.assertFalse(is_uppercase("hello"))

    def test_empty_string(self):
        self.assertFalse(is_uppercase(""))

    def test_numbers_and_symbols(self):
        self.assertFalse(is_uppercase("123!@#"))

    def test_uppercase_with_symbols(self):
        self.assertTrue(is_uppercase("HELLO!@#"))

if __name__ == '__main__':
    unittest.main()
