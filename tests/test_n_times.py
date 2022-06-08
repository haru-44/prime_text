import operator

from src.n_times import n_times


def test_n_times_mul():
    for a in range(5):
        for n in range(1, 5):
            assert n_times(a, n, operator.add) == a * n


def test_n_times_pow():
    for a in range(5):
        for n in range(1, 5):
            assert n_times(a, n, operator.mul) == a**n


def test_n_times_powmod():
    for a in range(5):
        for n in range(1, 5):
            assert n_times(a, n, lambda x, y: x*y % 7) == pow(a, n, 7)
