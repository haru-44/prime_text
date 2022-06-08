import math

from src.inverse_mod import inverse_mod


def test_inverse_mod_prime():
    for p in [2, 3, 101, 251]:
        for a in range(1, p):
            inv = inverse_mod(a, p)
            assert a * inv % p == 1


def test_inverse_mod_composite():
    for p in [6, 99, 250]:
        for a in range(1, p):
            inv = inverse_mod(a, p)
            if inv is None:
                assert math.gcd(a, p) != 1
            else:
                assert a * inv % p == 1
