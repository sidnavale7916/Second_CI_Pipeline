
import importlib

module = importlib.import_module("37_rotate_string")


def test_valid_rotation():
    assert module.is_rotation("abcd", "cdab") is True


def test_another_rotation():
    assert module.is_rotation("hello", "llohe") is True


def test_invalid_rotation():
    assert module.is_rotation("abcd", "abdc") is False


def test_different_lengths():
    assert module.is_rotation("abc", "abcd") is False


def test_empty_strings():
    assert module.is_rotation("", "") is True
