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
