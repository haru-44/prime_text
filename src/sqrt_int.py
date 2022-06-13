def sqrt_int(n: int) -> int:
    """ 整数nに対して、sqrt(n)の整数部分を返す。

    計算量 O(log log n)

    Args:
        n (int): 平方根を取る対象の自然数

    Returns:
        int: sqrt(n)の整数部分。

    Examples:
        >>> sqrt_int(26)
        5
        >>> sqrt_int(36)
        6
    """
    if n < 2:
        return n
    x = 2**((len(bin(n))-1)//2)
    while True:
        y = (x**2 + n) // (2 * x)
        if y >= x:
            return x
        x = y
