from typing import Tuple


def quadratic_form_reduction(a: int, b: int, c: int) -> Tuple[int, int, int]:
    """ 負の判別式を持つ2次形式(a,b,c)の簡約形式を返す。

    Args:
        a, b, c (int): 2次形式のパラメータ。ただし、判別式Dは負で平方数でないとする。

    Returns:
        a, b, c (int): 簡約形式
    """
    D = b**2 - 4 * a * c
    if D >= 0:
        raise ValueError()
    while True:
        if c < a:
            a, b, c = c, -b, a
        if a < b or b <= -a:
            b_ = b % (2 * a)
            if a < b_:
                b_ -= 2 * a
            c_ = (b_**2 - D) // (4 * a)
            a, b, c = a, b_, c_
        elif a == c and -a < b < 0:
            return a, -b, c
        else:
            return a, b, c
