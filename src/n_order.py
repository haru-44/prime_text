from sympy import factorint
from totient_function import totient_function


def n_order(a: int, n: int) -> int:
    """ 法nにおけるaの位数を求める。
    つまり、a^s = 1 (mod n)を満たす最小のsを求める。

    Args:
        a (int): 整数
        n (int): 正整数

    Returns:
        int: 法nにおけるaの位数
    """
    group_order = totient_function(n)
    order = group_order
    for prime in [*factorint(group_order)]:
        while pow(a, order // prime, n) == 1:
            order //= prime
    return order
