from typing import Tuple


def split_int(n: int) -> Tuple[int, int]:
    """ n = 2^s m を満たすs, mを計算する

    Args:
        n (int): 正整数

    Returns:
        s, m (int): n = 2**s * mを満たす整数

    Examples:
        >>> split_int(12)
        (2, 3)
        >>> split_int(16)
        (4, 1)
    """
    s, m = 0, n
    while m % 2 == 0:
        m //= 2
        s += 1
    return s, m
