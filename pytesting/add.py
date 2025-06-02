import pytest

def sum_of_two(a, b):
    return a + b

def test_add():
    assert sum_of_two(2, 3) == 5

def test_negative_add():
    assert sum_of_two(-2, 3) == 1