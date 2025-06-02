import pytest

def element_exists(lst, element):
    for item in lst:
        if item == element:
            return True
    return False

def test_element_present():
    assert element_exists([1, 2, 3, 4], 3)
    assert element_exists(["a", "b", "c"], "b")
    assert element_exists([None, True, False], None)

def test_element_not_present():
    assert not element_exists([1, 2, 3], 5)
    assert not element_exists(["x", "y"], "z")
    assert not element_exists([], "anything")

def test_duplicates():
    assert element_exists([1, 2, 2, 3], 2)
