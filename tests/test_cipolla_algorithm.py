from src.cipolla_algorithm import cipolla_algorithm, cipolla_algorithm_lucas
from sympy.ntheory import legendre_symbol


def test_cipolla_algorithm_01():
    for p in [3, 11, 101]:
        for a in range(1, p):
            if legendre_symbol(a, p) == 1:
                assert pow(cipolla_algorithm(a, p), 2, p) == a


def test_cipolla_algorithm_lucas_01():
    for p in [3, 11, 101]:
        for a in range(1, p):
            if legendre_symbol(a, p) == 1:
                assert pow(cipolla_algorithm_lucas(a, p), 2, p) == a
