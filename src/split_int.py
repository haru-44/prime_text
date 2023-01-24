def split_int(n: int, a: int = 2) -> tuple[int, int]:
    """ n = a^s m を満たすs, mを計算する。ただし、m は a で割り切れない

    Args:
        n (int): 正整数
        a (int): 2以上の整数

    Returns:
        s, m (int): n = a**s * mを満たす整数

    Examples:
        >>> split_int(12)
        (2, 3)
        >>> split_int(16)
        (4, 1)
    """
    s, m = 0, n
    while m % a == 0:
        m //= a
        s += 1
    return s, m
