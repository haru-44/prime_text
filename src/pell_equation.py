from continued_fraction import continued_fraction_sqrt


def pell_equation(n: int) -> tuple[int, int]:
    """ Pell方程式 x^2 - ny^2 = 1 を解く。

    Args:
        n (int): 平方数でない正整数

    Returns:
        x, y (int, int): x^2 - ny^2 = 1 を満たす最小解

    Examples:
        >>> pell_equation(2)
        (3, 2)
        >>> pell_equation(5)
        (9, 4)
    """
    cf = continued_fraction_sqrt(n)
    cf.__next__()
    while True:
        _, p, q, _ = cf.__next__()
        *_, Q = cf.__next__()
        if Q == 1:
            return p, q
