from src.miller_rabin_test import miller_rabin_test
from sympy.ntheory import isprime


def test_fermat_test_A001262():
    """
    Notes:
        https://oeis.org/A001262
    """
    pseudoprimes = [2047, 3277, 4033, 4681, 8321, 15841, 29341,
                    42799, 49141, 52633, 65281, 74665, 80581,
                    85489, 88357, 90751]

    for n in range(3, 100000, 2):
        ans = miller_rabin_test(n, a_list=[2])
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'


def test_fermat_test_A020229():
    """
    Notes:
        https://oeis.org/A020229
    """
    pseudoprimes = [121, 703, 1891, 3281, 8401, 8911, 10585,
                    12403, 16531, 18721, 19345, 23521, 31621,
                    44287, 47197, 55969, 63139, 74593, 79003,
                    82513, 87913, 88573, 97567]

    for n in range(5, 100000, 2):
        ans = miller_rabin_test(n, a_list=[3])
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'


def test_fermat_test_A020231():
    """
    Notes:
        https://oeis.org/A020231
    """
    pseudoprimes = [781, 1541, 5461, 5611, 7813, 13021, 14981,
                    15751, 24211, 25351, 29539, 38081, 40501,
                    44801, 53971, 79381]

    for n in range(7, 100000, 2):
        ans = miller_rabin_test(n, a_list=[5])
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'


def test_fermat_test_A020233():
    """
    Notes:
        https://oeis.org/A020233
    """
    pseudoprimes = [25, 325, 703, 2101, 2353, 4525, 11041, 14089,
                    20197, 29857, 29891, 39331, 49241, 58825, 64681,
                    76627, 78937, 79381, 87673, 88399, 88831]

    for n in range(9, 100000, 2):
        ans = miller_rabin_test(n, a_list=[7])
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'
