from src.solovay_strassen_test import solovay_strassen_test
from sympy.ntheory import isprime


def test_solovay_strassen_test_A047713():
    """
    Notes:
        https://oeis.org/A047713
    """
    pseudoprimes = [561, 1105, 1729, 1905, 2047, 2465, 3277, 4033,
                    4681, 6601, 8321, 8481, 10585, 12801, 15841, 16705,
                    18705]

    for n in range(3, 20000, 2):
        ans = solovay_strassen_test(n, a_list=[2])
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'


def test_solovay_strassen_test_A048950():
    """
    Notes:
        https://oeis.org/A048950
    """
    pseudoprimes = [121, 703, 1729, 1891, 2821, 3281, 7381, 8401,
                    8911, 10585, 12403, 15457, 15841, 16531, 18721,
                    19345]

    for n in range(5, 20000, 2):
        ans = solovay_strassen_test(n, a_list=[3])
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'
