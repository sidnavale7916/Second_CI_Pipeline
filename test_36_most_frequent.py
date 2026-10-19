import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent():
    assert module.most_frequent([1, 2, 2, 3]) == 2


def test_repeated_number():
    assert module.most_frequent([5, 5, 5, 1, 2]) == 5


def test_empty_list():
    assert module.most_frequent([]) is None


def test_equal_frequency():
    assert module.most_frequent([3, 2, 3, 2]) == 3