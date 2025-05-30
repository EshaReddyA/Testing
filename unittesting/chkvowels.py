import unittest

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

class TestCountVowels(unittest.TestCase):

    def test_normal_strings(self):
        self.assertEqual(count_vowels("hello"), 2)   
        self.assertEqual(count_vowels("world"), 1)   
        self.assertEqual(count_vowels("python"), 1)  

    def test_uppercase_vowels(self):
        self.assertEqual(count_vowels("HELLO"), 2)   
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("xyz"), 0)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_mixed_characters(self):
        self.assertEqual(count_vowels("123AE!"), 2)

if __name__ == '__main__':
    unittest.main()
