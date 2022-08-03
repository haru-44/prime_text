from src.sqrt_int import *


def test_sqrt_int_square():
    for i in range(100):
        assert i == sqrt_int(i**2)


def test_sqrt_int_square_p1():
    for i in range(1, 100):
        assert i == sqrt_int(i**2+1)


def test_sqrt_int_square_m1():
    for i in range(2, 100):
        assert i-1 == sqrt_int(i**2-1)


def test_sqrt_int_ceil_square():
    for i in range(100):
        assert i == sqrt_int_ceil(i**2)


def test_sqrt_int_ceil_square_p1():
    for i in range(1, 100):
        assert i + 1 == sqrt_int_ceil(i**2+1)


def test_sqrt_int_ceil_square_m1():
    for i in range(2, 100):
        assert i == sqrt_int_ceil(i**2-1)
