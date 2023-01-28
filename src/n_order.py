from sympy import factorint

from totient_function import totient_function


def n_order(a: int, n: int) -> int:
    """ 法nにおけるaの位数を求める。
    つまり、a^s = 1 (mod n)を満たす最小のsを求める。
    0 < a < n かつ gcd(a, n) = 1

    Args:
        a (int): 整数
        n (int): 正整数

    Returns:
        int: 法nにおけるaの位数

    Examples:
        >>> n_order(3, 11)
        5
        >>> n_order(5, 12)
        2
    """
    if a == 1:
        return 1
    group_order = totient_function(n)
    order = group_order
    for p, e in factorint(group_order).items():
        for _ in range(e):
            if pow(a, order // p, n) == 1:
                order //= p
            else:
                break
    return order
