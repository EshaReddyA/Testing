import pytest

def is_alphanumeric(s):
    return s.isalnum()

def test_all_letters():
    assert is_alphanumeric("HelloWorld")

def test_all_numbers():
    assert is_alphanumeric("123456")

def test_letters_and_numbers():
    assert is_alphanumeric("Hello123")

def test_with_space():
    assert not is_alphanumeric("Hello World")

def test_with_symbols():
    assert not is_alphanumeric("Hello!")

def test_empty_string():
    assert not is_alphanumeric("")
