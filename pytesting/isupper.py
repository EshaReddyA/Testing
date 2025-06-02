import pytest

def is_uppercase(s):
    return s.isupper()

def test_all_uppercase():
    assert is_uppercase("HELLO")

def test_mixed_case():
    assert not is_uppercase("Hello")

def test_all_lowercase():
    assert not is_uppercase("hello")

def test_empty_string():
    assert not is_uppercase("")

def test_numbers_and_symbols():
    assert not is_uppercase("123!@#")

def test_uppercase_with_symbols():
    assert is_uppercase("HELLO!@#")
