from src.lucas_lehmer_primality_test import lucas_lehmer_primality_test
from sympy.ntheory import primerange


def test_lucas_lehmer_primality_test_A000043():
    """
    Notes:
        https://oeis.org/A000043
    """
    correct = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]
    for p in primerange(3, 200):
        ret = lucas_lehmer_primality_test(p)
        assert (ret == 'prime number') == (p in correct)
