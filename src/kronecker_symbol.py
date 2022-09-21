import math

from jacobi_symbol import jacobi_symbol
from split_int import split_int


def kronecker_symbol(a: int, n: int) -> int:
    """ Kronecker記号(a / n)を計算する。

    Args:
        a (int): 整数
        n (int): 整数

    Returns:
        int: Kronecker記号(a / n)の値

    Examples:
        >>> kronecker_symbol(3, 10)
        1
        >>> kronecker_symbol(5, 8)
        -1
    """
    if math.gcd(a, n) != 1:
        return 0
    if n == 0:
        return 1
    sign = 1
    if n < 0:
        if a < 0:
            sign *= -1
        n *= -1
    s, m = split_int(n)
    a8 = a % 8
    if (a8 == 3 or a8 == 5) and s % 2 == 1:
        sign *= -1
    if m == 1:
        return sign
    return sign * jacobi_symbol(a, m)
