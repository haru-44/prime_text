import functools
import operator
from sympy.ntheory import factorint


def totient_function(n: int, n_is_prime: bool = False) -> int:
    """ Eulerのφ関数を計算する。

    Args:
        n (int): 対象の自然数
        n_is_prime (bool): nが予め素数であると分かっていればTrue

    Returns:
        int: φ(n)

    Examples:
        >>> totient_function(25)
        20
        >>> totient_function(1323)
        756
    """
    if n_is_prime:
        return n - 1
    ps = factorint(n)
    return functools.reduce(operator.mul, [p**e - p**(e - 1) for p, e in ps.items()])
