from typing import Tuple

from extended_gcd import extended_gcd
from quadratic_form_reduction import quadratic_form_reduction


def quadratic_form_composition(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int) -> Tuple[int, int, int]:
    """ 2つの2次形式を合成した2次形式を得る。

    Args:
        a1, b1, c1 (int): 2次形式のパラメータ。
        a2, b2, c2 (int): 2次形式のパラメータ。2つの2次形式の判別式は一致すること。

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
