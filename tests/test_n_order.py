import math

from src.n_order import n_order


def test_n_order_001():
    for n in range(2, 200):
        for a in range(1, n):
            if math.gcd(a, n) == 1:
                s = n_order(a, n)
                assert pow(a, s, n) == 1
                for k in range(2, s):
                    assert pow(a, k, n) != 1
