import pytest

def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 != 0) or (year % 400 == 0):
            return True
    return False

def test_leap_years():
    assert is_leap_year(2000)
    assert is_leap_year(2016)
    assert is_leap_year(2020)
    assert is_leap_year(2400)

def test_non_leap_years():
    assert not is_leap_year(1900)
    assert not is_leap_year(2019)
    assert not is_leap_year(2021)
    assert not is_leap_year(1800)
