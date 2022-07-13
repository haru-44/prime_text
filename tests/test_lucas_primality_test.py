from src.lucas_primality_test import lucas_primality_test
from sympy.ntheory import isprime


def test_lucas_primality_test_001():
    for n in range(3, 10000):
        assert (lucas_primality_test(n) == 'prime number') == isprime(n)
