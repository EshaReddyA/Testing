import unittest

def to_lowercase(s):
    return s.lower()

class TestToLowercase(unittest.TestCase):

    def test_all_uppercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")

    def test_mixed_case(self):
        self.assertEqual(to_lowercase("HeLLo WoRLd"), "hello world")

    def test_all_lowercase(self):
        self.assertEqual(to_lowercase("python"), "python")

    def test_numbers_and_symbols(self):
        self.assertEqual(to_lowercase("123!@#"), "123!@#")  

    def test_empty_string(self):
        self.assertEqual(to_lowercase(""), "")

if __name__ == '__main__':
    unittest.main()
