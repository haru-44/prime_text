from typing import Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """ 拡張Euclidの互除法によって、ax + by = gcd(a, b)を満たす整数x,yを求める

    Args:
        a, b (int): 最大公約数を求めたい2つの整数

    Returns:
        g, x, y (int): gはaとbの最大公約数。x,yはax + by = gを満たす整数

    Examples:
        >>> extended_gcd(3, 5)
        (1, 2, -1)
        >>> extended_gcd(25, 4)
        (1, 1, -6)
    """
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    assert (b % a) * x + a * y == g  # 左式が常に成り立つ
    q = b // a
    assert (b - q * a) * x + a * y == g  # (b % a) を (b - q * a) に置き換える
    assert a * (y - q * x) + b * x == g  # ax + by = g の形に整理する
    return g, y - q * x, x
