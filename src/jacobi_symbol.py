def jacobi_symbol(a: int, m: int) -> int:
    """ Jacobi記号(a / m)を計算する。

    Args:
        a (int): 整数
        m (int): 奇数

    Returns:
        int: Jacobi記号(a / m)の値

    Examples:
        >>> jacobi_symbol(2, 15)
        1
        >>> jacobi_symbol(5, 11)
        1
    """
    if a == 0:
        return 1 if m == 1 else 0
    if a % 2 == 1:
        sign = -1 if a % 4 == m % 4 == 3 else 1
        return sign * jacobi_symbol(m % a, a)
    sign = -1 if m % 8 == 3 or m % 8 == 5 else 1
    return sign * jacobi_symbol(a // 2, m)
