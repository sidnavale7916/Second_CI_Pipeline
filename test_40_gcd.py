
import importlib

module = importlib.import_module("40_gcd")


def test_common_divisor():
    assert module.gcd(12, 18) == 6


def test_another_pair():
    assert module.gcd(20, 30) == 10


def test_coprime_numbers():
    assert module.gcd(7, 13) == 1


def test_zero():
    assert module.gcd(0, 5) == 5


def test_negative_number():
    assert module.gcd(-12, 18) == 6


def test_both_zero():
    assert module.gcd(0, 0) == 0
