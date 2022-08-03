def nth_root_int(a: int, n: int) -> int:
    """ aのn乗根の整数部を求める

    Args:
        a (int): 0以上の整数
        n (int): 2以上の整数

    Returns:
        int: aのn乗根の整数部

    Examples:
        >>> nth_root_int(26, 3)
        2
    """
    if a < 2:
        return a
    x = 2**((a.bit_length() - 1 + n) // n)
    while True:
        y = (a + (n - 1) * x**n) // (n * x**(n - 1))
        if y >= x:
            return x
        x = y
