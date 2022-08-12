from src.pseudosquare_test import pseudosquare_test
from sympy.ntheory import isprime


def test_pseudosquare_test_001():
    for n in range(3, 10000, 2):
        result = pseudosquare_test(n)
        assert (result == 'prime number') == isprime(n)
