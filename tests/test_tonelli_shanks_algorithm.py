from src.tonelli_shanks_algorithm import tonelli_shanks_algorithm
from sympy.ntheory import legendre_symbol


def test_tonelli_shanks_algorithm_01():
    for p in [3, 11, 101]:
        for a in range(1, p):
            if legendre_symbol(a, p) == 1:
                assert pow(tonelli_shanks_algorithm(a, p), 2, p) == a
