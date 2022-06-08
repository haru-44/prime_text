import math

from src.gcd import *


def test_gcd_01():
    for a in range(0, 100, 5):
        for b in range(0, 100, 3):
            assert gcd(a, b) == math.gcd(a, b)


def test_gcd_02():
    for a in range(0, 100, 7):
        assert gcd(a, a+1) == math.gcd(a, a+1)
        assert gcd(a+1, a) == math.gcd(a+1, a)


def test_gcd_loop_01():
    for a in range(0, 100, 5):
        for b in range(0, 100, 3):
            assert gcd_loop(a, b) == math.gcd(a, b)


def test_gcd_loop_02():
    for a in range(0, 100, 7):
        assert gcd_loop(a, a+1) == math.gcd(a, a+1)
        assert gcd_loop(a+1, a) == math.gcd(a+1, a)
