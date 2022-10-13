import math

from src.sqrt_modulo import *
from sympy.ntheory import factorint, jacobi_symbol, primerange


def test_sqrt_modulo_pe_001():
    for p in primerange(3, 30):
        for e in range(1, 5):
            for a in range(1, min(30, p**e)):
                if jacobi_symbol(a, p) != 1:
                    continue
                x = sqrt_modulo_pe(a, p, e)
                assert pow(x, 2, p**e) == a


def test_sqrt_modulo_n_001():
    for n in range(3, 500, 2):
        for a in range(1, n):
            if math.gcd(a, n) != 1:
                continue
        for x in sqrt_modulo_n(a, factorint(n)):
            assert pow(x, 2, n) == a
