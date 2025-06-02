import pytest

def last_element(lst):
    try:
        return lst[-1]
    except IndexError:
        raise ValueError("List is empty")

def test_regular_list():
    assert last_element([1, 2, 3, 4]) == 4
    assert last_element(["a", "b", "c"]) == "c"
    assert last_element([True, False, True]) == True

def test_single_element_list():
    assert last_element([42]) == 42
    assert last_element(["hello"]) == "hello"

def test_empty_list():
    with pytest.raises(ValueError):
        last_element([])
