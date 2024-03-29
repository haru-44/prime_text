import math
from typing import Generator

from sympy.ntheory import sqrt_mod

from sqrt_int import sqrt_int


def quadratic_form_class_number_naive(D: int) -> Generator[tuple[int, int, int], None, None]:
    """ 判別式Dに対するC(D) の元を枚挙する。

    Args:
        D (int): 判別式。D < 0 かつ D = 0,1 (mod 4)

    Yields:
        a, b, c (int, int, int): 2次形式

    Examples:
        >>> list(quadratic_form_class_number_naive(-3))
        [(1, 1, 1)]
        >>> list(quadratic_form_class_number_naive(-23))
        [(1, 1, 6), (2, 1, 3), (2, -1, 3)]
    """
    if D >= 0:
        raise ValueError()
    for a in range(1, sqrt_int(-D // 3) + 1):
        for b in filter(lambda x: x <= a, sqrt_mod(D, 4 * a, all_roots=True)):
            c = (b**2 - D) // (4 * a)
            if c < a or math.gcd(math.gcd(a, b), c) != 1:
                continue
            yield (a, b, c)
            if a != b and a != c and b != 0:
                yield (a, -b, c)
