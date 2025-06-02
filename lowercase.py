import pytest

def to_lowercase(s):
    return s.lower()

def test_all_uppercase():
    assert to_lowercase("HELLO") == "hello"

def test_mixed_case():
    assert to_lowercase("HeLLo WoRLd") == "hello world"

def test_all_lowercase():
    assert to_lowercase("python") == "python"

def test_numbers_and_symbols():
    assert to_lowercase("123!@#") == "123!@#"

def test_empty_string():
    assert to_lowercase("") == ""
