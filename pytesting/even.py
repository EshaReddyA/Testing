import pytest

def is_even(n):
    return n % 2 == 0

def test_even_numbers():
    assert is_even(2)
    assert is_even(10)
    assert is_even(0)
    assert is_even(-4)

def test_odd_numbers():
    assert not is_even(1)
    assert not is_even(7)
    assert not is_even(-3)
