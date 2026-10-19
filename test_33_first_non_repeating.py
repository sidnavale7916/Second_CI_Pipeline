import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating():
    assert module.first_non_repeating("swiss") == "w"


def test_first_character_unique():
    assert module.first_non_repeating("hello") == "h"


def test_no_unique_character():
    assert module.first_non_repeating("aabb") is None