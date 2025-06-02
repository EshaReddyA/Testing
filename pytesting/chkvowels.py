import pytest
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def test_normal_strings():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("python") == 1

def test_uppercase_vowels():
    assert count_vowels("HELLO") == 2
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("xyz") == 0

def test_empty_string():
    assert count_vowels("") == 0

def test_mixed_characters():
    assert count_vowels("123AE!") == 2
