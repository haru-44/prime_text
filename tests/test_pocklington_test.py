from src.pocklington_test import pocklington_test
from sympy.ntheory import factorint, isprime


def test_pocklington_test_001():
    for n in range(3, 1000):
        ans = pocklington_test(n, factorint(n-1).keys(), k=100)
        assert isprime(n) == (ans == 'prime number')
