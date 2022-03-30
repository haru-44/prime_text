def sqrt_int(n: int) -> int:
    """ 整数nに対して、sqrt(n)の整数部分を返す。

    計算量 O(ln ln n)

    Args:
        n (int): 平方根を取る対象の自然数

    Returns:
        int: sqrt(n)の整数部分。ただし、n=0の場合は、0とする

    Examples:
        >>> sqrt_int(26)
        5
        >>> sqrt_int(36)
        6
    """
    if n == 0:
        return 0
    x = n
    while True:
        y = (x**2 + n) // (2 * x)
        if y >= x:
            return x
        x = y
