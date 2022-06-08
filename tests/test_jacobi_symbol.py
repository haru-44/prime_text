from src.jacobi_symbol import jacobi_symbol
from sympy.ntheory import primerange


def test_jacobi_symbol_A034947():
    """
    Notes:
        https://oeis.org/A034947
    """
    correct = [1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1,
               1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1]
    for idx in range(0, len(correct), 2):
        assert jacobi_symbol(-1, idx+1) == correct[idx]


def test_jacobi_symbol_A191018():
    """
    Notes:
        https://oeis.org/A191018
    """
    correct = [2, 17, 19, 23, 31, 47, 53, 61, 79, 83, 107, 109,
               113, 137, 139, 151, 167, 173, 181, 197, 199]
    for p in primerange(0, 200):
        ret = jacobi_symbol(p, 15)
        if p in correct:
            assert ret == 1
        else:
            assert ret != 1


def test_jacobi_symbol_A191026():
    """
    Notes:
        https://oeis.org/A191026
    """
    correct = [3, 11, 13, 17, 29, 47, 71, 73, 79, 83, 97, 103,
               109, 149, 151, 157, 167, 173, 179, 191]
    for p in primerange(0, 200):
        ret = jacobi_symbol(p, 35)
        if p in correct:
            assert ret == 1
        else:
            assert ret != 1
