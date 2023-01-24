from extended_gcd import extended_gcd


def chainese_remainder_theorem(congruent_exps: list[tuple[int, int]]) \
        -> tuple[int, int] | None:
    """ 中国の剰余定理を用いて、連立合同式を解く。

    Args:
        congruent_exps ([(int, int)]): 合同式のリスト

    Returns:
        r, M ((int, int) or None): congruent_expsを満たすような r (mod M)
                                     存在しなければ None

    Examples:
        >>> # r = 2 (mod 3)
        >>> # r = 4 (mod 5)
        >>> # を満たすような r (mod M) を求める。
        >>> chainese_remainder_theorem([(2, 3), (4, 5)])
        (14, 15)
    """
    r, M = 0, 1
    for var, mod in congruent_exps:
        g, x, _ = extended_gcd(M, mod)
        if (var - r) % g != 0:
            return None
        rem = mod // g
        r += M * (var - r) // g * (x % rem)
        M *= rem
    return r % M, M
