import math

from src.n_order import n_order
from sympy import ntheory


def test_n_order_001():
    for n in range(2, 100):
        for a in range(1, n):
            if math.gcd(a, n) == 1:
                assert n_order(a, n) == ntheory.n_order(a, n)
