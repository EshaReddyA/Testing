import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def test_positive_numbers():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_negative_numbers():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5

def test_float_result():
    assert divide(7, 2) == 3.5
    assert divide(1, 4) == 0.25

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_zero_numerator():
    assert divide(0, 5) == 0
