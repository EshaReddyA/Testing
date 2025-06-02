import pytest

def max_of_three(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c

def test_all_positive():
    assert max_of_three(1, 5, 3) == 5
    assert max_of_three(10, 20, 15) == 20

def test_all_negative():
    assert max_of_three(-1, -5, -3) == -1
    assert max_of_three(-10, -20, -15) == -10
