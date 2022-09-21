from kronecker_symbol import kronecker_symbol


def dirichlet_class_number_formula(D: int) -> int:
    """ 虚2次体の場合について、Dirichletの類数公式を計算する。

    Args:
        D (int): D < 0 で次のどちらかを満たす。
                    ・D = 1 (mod 4) かつ Dは平方因子を持たない
                    ・D = 8,12 (mod 16) かつ D/4は平方因子を持たない

    Returns:
        int: 2次体の類数

    Examples:
        >>> dirichlet_class_number_formula(-47)
        5
    """
    assert D < 0
    h = 0
    for n in range(1, abs(D)):
        h += kronecker_symbol(D, n) * n
    if D == -3:
        w = 3
    elif D == -4:
        w = 2
    else:
        w = 1
    return h * w // D


def dirichlet_class_number_formula_simplify(D: int) -> int:
    """ 虚2次体の場合について、Dirichletの類数公式を計算する(計算量削減版)。

    Args:
        D (int): D < -4 で次のどちらかを満たす。
                    ・D = 1 (mod 4) かつ Dは平方因子を持たない
                    ・D = 8,12 (mod 16) かつ D/4は平方因子を持たない

    Returns:
        int: 2次体の類数

    Examples:
        >>> dirichlet_class_number_formula_simplify(-47)
        5
    """
    assert D < -4
    h = sum(kronecker_symbol(D, n) for n in range(1, abs(D) // 2 + 1))
    if D % 8 == 5:
        h //= 3
    elif D % 4 == 0:
        h //= 2
    return h
