from src.aks_test import aks_test
from sympy.ntheory import isprime


def test_aks_test_001():
    for n in range(2, 2**10):
        assert (aks_test(n) == 'prime number') == isprime(n)
