from jacobi_symbol import jacobi_symbol


def elliptic_curve_order_naive(a: int, b: int, p: int) -> int:
    """ 楕円曲線 y**2 = x**3 + a*x + b (mod p) の群の位数を計算する。

    Args:
        a: int, b: int: 楕円曲線のパラメータ。y**2 = x**3 + a * x + b
        p (int): p > 3となる素数。

    Return:
        int: 群の位数

    Examples:
        >>> elliptic_curve_order_naive(1, 3, 5)
        4
        >>> elliptic_curve_order_naive(1, 1, 5)
        9
    """
    if (4 * a**3 + 27 * b**2) % p == 0:
        return ValueError()
    return p + 1 + sum(jacobi_symbol(x**3 + a * x + b, p) for x in range(p))
