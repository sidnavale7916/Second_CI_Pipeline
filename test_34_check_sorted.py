import importlib

module = importlib.import_module("34_check_sorted")


def test_sorted_list():
    assert module.is_sorted([1, 2, 3, 4]) is True


def test_unsorted_list():
    assert module.is_sorted([5, 2, 8]) is False


def test_duplicate_numbers():
    assert module.is_sorted([1, 1, 2, 3]) is True


def test_empty_list():
    assert module.is_sorted([]) is True