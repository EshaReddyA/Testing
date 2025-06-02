import unittest

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

class TestAreAnagrams(unittest.TestCase):

    def test_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))

    def test_not_anagrams(self):
        self.assertFalse(are_anagrams("hello", "world"))

    def test_same_string(self):
        self.assertTrue(are_anagrams("python", "python"))

    def test_different_lengths(self):
        self.assertFalse(are_anagrams("abc", "ab"))

    def test_case_sensitive(self):
        self.assertFalse(are_anagrams("Listen", "silent"))

if __name__ == '__main__':
    unittest.main()

