from src.fermat_factorization_method_fast import \
    fermat_factorization_method_fast
from sympy.ntheory import primerange


def test_fermat_factorization_method_fast_001():
    for r in range(5, 1000, 2):
        for s in range(5, 1000, 2):
            n = r * s
            if n % 3 == 0:
                continue
            result = fermat_factorization_method_fast(n)
            assert result != 1
            assert n % result == 0


def test_fermat_factorization_method_fast_002():
    for p in primerange(5, 10000):
        assert fermat_factorization_method_fast(p) == 1
