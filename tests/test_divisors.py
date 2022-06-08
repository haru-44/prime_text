from src.divisors import divisors
from sympy.ntheory import primerange


def test_divisors_prime():
    for p in primerange(2, 100):
        assert divisors(p) == [1, p]


def test_divisors_A000396():
    """ 完全数を確認する
    Notes:
        https://oeis.org/A000396
    """
    correct = [6, 28, 496, 8128]
    for n in correct:
        assert sum(divisors(n)) == 2*n


def test_divisors_A063990():
    """ 友愛数を確認する
    Notes:
        https://oeis.org/A063990
    """
    correct = [(220, 284), (1184, 1210), (2620, 2924),
               (5020, 5564), (6232, 6368), (10744, 10856)]
    for n, m in correct:
        assert sum(divisors(n))-n == m
        assert sum(divisors(m))-m == n
