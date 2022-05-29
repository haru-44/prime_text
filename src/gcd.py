def gcd(a: int, b: int) -> int:
    """ Euclidの互除法を用いて、aとbの最大公約数を求める。

    Args:
        a, b (int): 最大公約数を求めたい2つの整数

    Returns:
        g (int): aとbの最大公約数

    Examples:
        >>> gcd(15, 20)
        5
        >>> gcd(3, 7)
        1
    """
    if a == 0:
        return b
    return gcd(b % a, a)


def gcd_loop(a: int, b: int) -> int:
    """ Euclidの互除法を用いて、aとbの最大公約数を求める。非再帰版。

    Args:
        a, b (int): 最大公約数を求めたい2つの整数

    Returns:
        g (int): aとbの最大公約数

    Examples:
        >>> gcd_loop(15, 20)
        5
        >>> gcd_loop(3, 7)
        1
    """
    while b > 0:
        a, b = b, a % b
    return a
