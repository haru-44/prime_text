from src.lucas_sequence import *


def test_lucas_sequence_fibonacci():
    """ Lucas数列(a=1,b=-1) U_n を調べる。a.k.a. Fibnacci数列

    Notes:
        https://oeis.org/A000045
    """
    correct = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
               377, 610, 987, 1597, 2584, 4181, 6765]
    for n in range(len(correct)):
        assert lucas_sequence_u(n, a=1, b=-1) == correct[n]


def test_lucas_sequence_periodic():
    """ Lucas数列(a=1,b=1) U_n を調べる。

    Notes:
        https://oeis.org/A128834
    """
    correct = [0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0,
               -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1]
    for n in range(len(correct)):
        assert lucas_sequence_u(n, a=1, b=1) == correct[n]


def test_lucas_sequence_A107920():
    """ Lucas数列(a=1,b=2) U_n を調べる。

    Notes:
        https://oeis.org/A107920
    """
    correct = [0, 1, 1, -1, -3, -1, 5, 7, -3, -17, -11, 23, 45,
               -1, -91, -89, 93, 271, 85, -457, -627, 287, 1541]
    for n in range(len(correct)):
        assert lucas_sequence_u(n, a=1, b=2) == correct[n]


def test_lucas_sequence_A006190():
    """ Lucas数列(a=3,b=-1) U_n を調べる。

    Notes:
        https://oeis.org/A006190
    """
    correct = [0, 1, 3, 10, 33, 109, 360, 1189, 3927, 12970,
               42837, 141481, 467280, 1543321, 5097243, 16835050]
    for n in range(len(correct)):
        assert lucas_sequence_u(n, a=3, b=-1) == correct[n]


def test_lucas_sequence_lucas_numbers():
    """ Lucas数列(a=1,b=-1) V_n を調べる。 a.k.a. Lucas数

    Notes:
        https://oeis.org/A000032
    """
    correct = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322,
               521, 843, 1364, 2207, 3571, 5778, 9349, 15127]
    for n in range(len(correct)):
        assert lucas_sequence_v(n, a=1, b=-1) == correct[n]


def test_lucas_sequence_lucas_A002249():
    """ Lucas数列(a=1,b=2) V_n を調べる。

    Notes:
        https://oeis.org/A002249
    """
    correct = [2, 1, -3, -5, 1, 11, 9, -13, -31, -5, 57, 67, -47,
               -181, -87, 275, 449, -101, -999, -797, 1201, 2795]
    for n in range(len(correct)):
        assert lucas_sequence_v(n, a=1, b=2) == correct[n]


def test_lucas_sequence_lucas_A201455():
    """ Lucas数列(a=3,b=-4) V_n を調べる。

    Notes:
        https://oeis.org/A201455
    """
    correct = [2, 3, 17, 63, 257, 1023, 4097, 16383, 65537, 262143,
               1048577, 4194303, 16777217, 67108863, 268435457]
    for n in range(len(correct)):
        assert lucas_sequence_v(n, a=3, b=-4) == correct[n]
