from src.fermat_factorization_method import fermat_factorization_method
from sympy.ntheory import primerange


def test_fermat_factorization_method_001():
    for r in range(3, 100, 2):
        for s in range(3, 100, 2):
            n = r * s
            result = fermat_factorization_method(n)
            assert result != 1
            assert n % result == 0


def test_fermat_factorization_method_002():
    for p in primerange(3, 100):
        assert fermat_factorization_method(p) == 1
