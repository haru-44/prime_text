import math

from sympy.ntheory import sqrt_mod

from is_square_number import is_square_number
from nth_root_int import nth_root_int
from sqrt_int import sqrt_int


def mckee_method(n: int) -> int:
    """ Mckee 法によって n の因数を求める。

    Args:
        n (int): 因数分解する整数で、
                 n > 1 かつ 3n^{1/3}より小さい素因数はないとする。

    Returns:
        int: n の因数。n が素数の場合は1

    Examples:
        >>> mckee_method(101 * 107)
        101
        >>> mckee_method(11) # 素数の場合は1
        1
    """
    if is_square_number(n):
        return sqrt_int(n)
    # x0 = int((n - n**(2/3))**(1/2)) と厳密には異なるが特に問題ない
    x0 = sqrt_int(n - nth_root_int(n, 3)**2)
    D = 4 * (n - x0**2)
    if ((2 * x0)**2 + D) % (4 * n) != 0:
        raise ValueError()
    if math.gcd(n, D) > 1:
        return math.gcd(n, D)
    for a in range(1, sqrt_int(D // 3) + 1):
        an4 = 4 * a * n
        for u_ in sqrt_mod(an4, D, all_roots=True):
            for u in range(u_, sqrt_int(an4) + 1, D):
                v2 = (an4 - u**2) // D
                if is_square_number(v2):
                    vx = 2 * x0 * sqrt_int(v2)
                    if vx % (2 * n) != u and -vx % (2 * n) != u:
                        return math.gcd(vx - u, n)
    return 1
