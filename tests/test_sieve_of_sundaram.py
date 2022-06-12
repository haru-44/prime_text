from src.sieve_of_sundaram import sieve_of_sundaram
from sympy.ntheory import primerange


def test_sieve_of_sundaram_001():
    for n in [11, 101, 1001, 10001]:
        assert sieve_of_sundaram(n) == list(primerange(3, n+1))
