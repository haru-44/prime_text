from src.proth_test import *
from src.split_int import split_int

A080076 = [3, 5, 13, 17, 41, 97, 113, 193, 241, 257, 353,
           449, 577, 641, 673, 769, 929, 1153, 1217, 1409,
           1601, 2113, 2689, 2753, 3137, 3329, 3457, 4481,
           4993, 6529]
correct = [2, 2, 2, 3, 3, 5, 3, 5, 7, 3, 3, 3, 5, 3, 5, 7, 3,
           5, 3, 3, 3, 5, 13, 3, 3, 3, 5, 3, 5, 7]


def test_proth_test_A248972():
    """
    Notes:
        https://oeis.org/A248972
    """
    for n, a in zip(A080076, correct):
        s, m = split_int(n - 1)
        assert proth_test(s, m, a_list=[a]) == 'prime number'


def test_proth_test_3_A248972():
    """
    Notes:
        https://oeis.org/A248972
    """
    for n in A080076:
        s, m = split_int(n - 1)
        if n == 3 or m % 3 == 0:
            continue
        assert proth_test_3(s, m) == 'prime number'
