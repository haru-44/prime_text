from src.sieve_of_eratosthenes import sieve_of_eratosthenes
from sympy.ntheory import isprime

def test_sieve_of_eratosthenes_01():
    for n in [2, 100, 1000]:
        li = sieve_of_eratosthenes(n)
        for i in range(1, n+1):
            assert li[i] == isprime(i)
