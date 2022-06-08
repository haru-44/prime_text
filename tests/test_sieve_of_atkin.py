from src.sieve_of_atkin import sieve_of_atkin
from sympy.ntheory import isprime

def test_sieve_of_atkin_01():
    for n in [5, 100, 1000]:
        li = sieve_of_atkin(n)
        for i in range(1, n+1):
            assert li[i] == isprime(i)
