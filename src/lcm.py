from gcd import gcd


def lcm(a: int, b: int) -> int:
    """ aとbの最小公倍数を求める。

    Args:
        a, b (int): 最小公倍数を求めたい2つの整数

    Returns:
        int : aとbの最小公倍数

    Examples:
        >>> lcm(4, 6)
        12
        >>> lcm(4, 9)
        36
    """
    return a * b // gcd(a, b)
