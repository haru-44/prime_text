from typing import Optional, Tuple

from cipolla_algorithm import cipolla_algorithm
from is_square_number import is_square_number
from jacobi_symbol import jacobi_symbol
from sqrt_int import sqrt_int


def cornacchia_smith(p: int, d: int) -> Optional[Tuple[int, int]]:
    """ Cornacchia-Smith 法で、p = x^2+dy^2 を満たすx,yを求める。

    (x,y)が解なら(-x,y),(x,-y),(-x,-y)も解であるが、(x,y)のみを返す。

    Args:
        p (int): 奇素数
        d (int): pで割り切れない正整数

    Returns:
        x, y (int, int): p = x^2+dy^2 を満たすx,y
                         そのようなx,yが存在しないならNone

    Examples:
        >>> cornacchia_smith(101, 4) # 101 = 1^2 + 4 * 5^2
        (1, 5)
    """
    if jacobi_symbol(-d, p) == -1:
        return None
    x = p - cipolla_algorithm(-d, p)  # -dの平方根のうち、2x>pを満たす方を使う
    a, b = p, x
    c = sqrt_int(p)
    while c < b:
        a, b = b, a % b
    t = p - b**2
    if t % d != 0:
        return None
    t //= d
    if is_square_number(t):
        return b, sqrt_int(t)
    else:
        return None


def cornacchia_smith_4p(p: int, d: int) -> Optional[Tuple[int, int]]:
    """ Cornacchia-Smith 法で、4p = x^2+|d|y^2 を満たすx,yを求める。

    (x,y)が解なら(-x,y),(x,-y),(-x,-y)も解であるが、(x,y)のみを返す。

    Args:
        p (int): 素数
        d (int): -4p < d < 0 かつ d = 0,1 (mod 4)

    Returns:
        x, y (int, int): 4p = x^2+|d|y^2 を満たすx,y
                         そのようなx,yが存在しないならNone

    Examples:
        >>> cornacchia_smith_4p(101, -323) # 4 * 101 = 9^2 + 323 * 1^2
        (9, 1)
    """
    if p == 2:
        if is_square_number(d + 8):
            return sqrt_int(d + 8), 1
        else:
            return None
    if jacobi_symbol(d, p) != 1:
        return None
    x = cipolla_algorithm(d, p)
    # x = d (mod 4p) を保証する
    if x % 2 != d % 2:
        x = p - x
    a, b = 2*p, x
    c = sqrt_int(4 * p)
    while c < b:
        a, b = b, a % b
    t = 4*p - b**2
    if t % abs(d) != 0:
        return None
    t //= abs(d)
    if is_square_number(t):
        return b, sqrt_int(t)
    else:
        return None
