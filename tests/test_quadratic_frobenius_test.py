import math

from src.quadratic_frobenius_test import quadratic_frobenius_test
from src.selfridge_method_a import selfridge_method_a
from src.sqrt_int import sqrt_int
from sympy.ntheory import isprime


def test_odd_fibonacci_pseudoprimes():
    """ Fibonacci擬素数を10000未満について調べる

    Notes:
        https://oeis.org/A081264
    """
    pseudoprimes = [323, 377, 1891, 3827, 4181, 5777, 6601, 6721, 8149]
    for n in range(2, 10000):
        if math.gcd(n, 10) != 1:
            continue
        ans = quadratic_frobenius_test(n, a=1, b=-1, method='lucas')
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'


def test_lucas_pseudoprimes():
    """ Lucas擬素数を10000未満について調べる

    Notes:
        https://oeis.org/A217120
    """
    pseudoprimes = [323, 377, 1159, 1829, 3827, 5459, 5777, 9071, 9179]
    for n in range(3, 10000, 2):
        if sqrt_int(n)**2 == n:
            continue
        a, b = selfridge_method_a(n)
        if a == 0 and b == 0:
            continue
        if math.gcd(n, 2*a*b*(a**2-4*b)) != 1:
            continue
        ans = quadratic_frobenius_test(n, a, b, method='lucas')
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'


def test_frobenius_pseudoprimes():
    """ x^2-x-1のFrobenius擬素数を10000未満について調べる

    Notes:
        https://oeis.org/A212424
    """
    pseudoprimes = [4181, 5777, 6721]
    for n in range(2, 10000):
        if math.gcd(n, 10) != 1:
            continue
        ans = quadratic_frobenius_test(n, a=1, b=-1)
        if isprime(n):
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'
