def nth_root_int(a: int, n: int) -> int:
    """ aのn乗根の整数部を求める

    Args:
        a, b (int): パラメータ

    Returns:
        int: aのn乗根の整数部

    Examples:
        >>> nth_root_int(26, 3)
        2
    """
    if a == 0:
        return 0
    x = a
    while True:
        y = (a + (n - 1) * x**n) // (n * x**(n - 1))
        if y >= x:
            return x
        x = y
