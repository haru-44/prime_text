from functools import lru_cache


@lru_cache(maxsize=None)
def lucas_sequence_u(n: int, a: int, b: int) -> int:
    """ Lucas数列のn番目U_nを計算する。

    Args:
        n (int): n番目のLucas数列を求める
        a, b (int): Lucas数列のパラメータ

    Returns:
        int: n番目のLucas数列の値

    Examples:
        >>> lucas_sequence(4, 3, 2)
        15
        >>> lucas_sequence(5, 6, 7)
        589
    """
    if n <= 1:
        return n
    return a * lucas_sequence_u(n - 1, a, b) - b * lucas_sequence_u(n - 2, a, b)


@lru_cache(maxsize=None)
def lucas_sequence_v(n: int, a: int, b: int) -> int:
    """ Lucas数列のn番目V_nを計算する。

    Args:
        n (int): n番目のLucas数列を求める
        a, b (int): Lucas数列のパラメータ

    Returns:
        int: n番目のLucas数列の値

    Examples:
        >>> lucas_sequence(4, 3, 2)
        17
        >>> lucas_sequence(5, 6, 7)
        1686
    """
    if n == 0:
        return 2
    if n == 1:
        return a
    return a * lucas_sequence_v(n - 1, a, b) - b * lucas_sequence_v(n - 2, a, b)
