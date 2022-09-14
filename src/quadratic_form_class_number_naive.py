import math
from typing import Generator, Tuple

from sqrt_int import sqrt_int


def quadratic_form_class_number_naive(D: int) -> Generator[Tuple[int, int, int], None, None]:
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
    assert D < 0 and (D % 4 == 0 or D % 4 == 1)
    for a in range(1, sqrt_int(-D // 3) + 1):
        for b in range(a + 1):
            c, r = divmod(b**2 - D, 4 * a)
            if r != 0 or c < a or math.gcd(math.gcd(a, b), c) != 1:
                continue
            yield (a, b, c)
            if a != b and a != c and b != 0:
                yield (a, -b, c)
