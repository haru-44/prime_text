from typing import Tuple

from extended_gcd import extended_gcd
from quadratic_form_reduction import quadratic_form_reduction


def quadratic_form_composition(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int) -> Tuple[int, int, int]:
    """ 2つの2次形式を合成した2次形式を得る。

    Args:
        a1, b1, c1 (int): 2次形式のパラメータ。
        a2, b2, c2 (int): 2次形式のパラメータ。2つの2次形式の判別式は一致し、負であること。

    Returns:
        a3, b3, c3 (int): 2つの2次形式の合成。ただし、簡約形式である。
    """
    D = b1**2 - 4 * a1 * c1
    h, _, v = extended_gcd(a1, a2)
    g, u, w = extended_gcd(h, (b1 + b2) // 2)
    a3 = (a1 * a2) // g**2
    b3 = b2 + 2 * a2 * ((b1 - b2) // 2 * v * u - c2 * w) // g
    c3 = (b3**2 - D) // (4 * a3)
    return quadratic_form_reduction(a3, b3, c3)


def quadratic_form_composition2(a: int, b: int, c: int) -> Tuple[int, int, int]:
    """ 2次形式(a,b,c)の2乗を計算する。

    Args:
        a, b, c (int): 2次形式のパラメータ。判別式は負であること。

    Returns:
        a_, b_, c_ (int): 2次形式(a,b,c)の2乗。
    """
    D = b**2 - 4 * a * c
    g, _, w = extended_gcd(a, b)
    k = a // g
    a_ = k**2
    b_ = b - 2 * k * c * w
    c_ = (b_**2 - D) // (4 * a_)
    return quadratic_form_reduction(a_, b_, c_)


def quadratic_form_composition3(a: int, b: int, c: int) -> Tuple[int, int, int]:
    """ 2次形式(a,b,c)の3乗を計算する。

    Args:
        a, b, c (int): 2次形式のパラメータ。判別式は負であること。

    Returns:
        a_, b_, c_ (int): 3次形式(a,b,c)の3乗。
    """
    D = b**2 - 4 * a * c
    g, _, w = extended_gcd(a, b)
    k = a // g
    a_ = k**2
    t = k * c * w
    h, _, V = extended_gcd(a_, a)
    g, U, w = extended_gcd(h, b - t)
    k = a // g
    a_ = a_ * k // g
    t = k * (t * V * U + c * w)
    b_ = b - 2 * t
    c_ = (b_**2 - D) // (4 * a_)
    return quadratic_form_reduction(a_, b_, c_)
