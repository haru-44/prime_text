from src.find_qnr import find_qnr
from sympy.ntheory import jacobi_symbol, primerange


def test_find_qnr_001():
    for p in primerange(3, 100):
        a = find_qnr(p)
        assert jacobi_symbol(a, p) == -1
