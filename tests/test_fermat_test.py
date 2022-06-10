from src.fermat_test import fermat_test
from sympy.ntheory import isprime


def test_fermat_test_A001567():
    """
    Notes:
        https://oeis.org/A001567
    """
    pseudoprimes = [341, 561, 645, 1105, 1387, 1729, 1905, 2047,
                    2465, 2701, 2821, 3277, 4033, 4369, 4371, 4681,
                    5461, 6601, 7957, 8321, 8481, 8911]

    for n in range(3, 10000):
        ans = fermat_test(n, a_list=[2])
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'


def test_fermat_test_A020136():
    """
    Notes:
        https://oeis.org/A020136
    """
    pseudoprimes = [15, 85, 91, 341, 435, 451, 561, 645, 703, 1105,
                    1247, 1271, 1387, 1581, 1695, 1729, 1891, 1905,
                    2047, 2071, 2465, 2701, 2821, 3133, 3277, 3367,
                    3683, 4033, 4369, 4371, 4681, 4795, 4859]

    for n in range(5, 5000):
        ans = fermat_test(n, a_list=[4])
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'
