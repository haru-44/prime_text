from extended_gcd import extended_gcd
from typing import Optional


def inverse_mod(a: int, n: int) -> Optional[int]:
    """ 法nにおけるaの逆元xを返す。つまり、xはa * x = 1 (mod n)を満たす。

    Args:
        a (int): 逆元をもとめる数
        n (int): 法

    Returns:
        x (int or None): a * x = 1  (mod n)を満たす整数 1 <= x < n
                         そのようなxが存在しないとき、None

    Examples:
        >>> inverse_mod(3, 5)
        2
        >>> inverse_mod(2, 4)
    """
    a %= n
    g, x, _ = extended_gcd(a, n)
    if g == 1:
        return x % n
