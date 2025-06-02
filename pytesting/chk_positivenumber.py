import pytest

def is_positive(n):
    return n > 0

def test_positive_numbers():
    assert is_positive(1)
    assert is_positive(10)
    assert is_positive(0.5)

def test_zero():
    assert not is_positive(0)

def test_negative_numbers():
    assert not is_positive(-1)
    assert not is_positive(-0.5)
