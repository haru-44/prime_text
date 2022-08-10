from sqrt_int import sqrt_int, sqrt_int_ceil


def fermat_factorization_method(n: int) -> int:
    """ Fermat法による素因数分解を行う。

    Args:
        n (int): 素因数分解する奇数

    Returns:
        int: nが合成数の場合は、nの非自明な約数
             nが素数の場合は、1

    Examples:
        >>> fermat_factorization_method(2021) # 2021 = 43 * 47
        43
        >>> fermat_factorization_method(2019) # 2019 = 3 * 673
        3
        >>> fermat_factorization_method(2027) # 2027 is prime
        1
    """
    assert n % 2 == 1
    for x in range(sqrt_int_ceil(n), (n + 9) // 6 + 1):
        y2 = x**2 - n
        y = sqrt_int(y2)
        if y**2 == y2:
            return x - y
    return 1
