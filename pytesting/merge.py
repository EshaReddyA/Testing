import pytest

def merge_lists(list1, list2):
    return list1 + list2

def test_regular_lists():
    assert merge_lists([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert merge_lists(["a", "b"], ["c", "d"]) == ["a", "b", "c", "d"]

def test_empty_first_list():
    assert merge_lists([], [1, 2, 3]) == [1, 2, 3]

def test_empty_second_list():
    assert merge_lists([1, 2, 3], []) == [1, 2, 3]

def test_both_empty():
    assert merge_lists([], []) == []

def test_with_duplicates():
    assert merge_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]

