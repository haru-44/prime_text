from src.factor_sieve import factor_sieve
from sympy.ntheory import factorint, isprime


def test_factor_sieve_001():
    sieve = factor_sieve(100000)
    for n in range(2, len(sieve)):
        if isprime(n):
            assert sieve[n] == 1
        else:
            assert sieve[n] == min([*factorint(n)])
