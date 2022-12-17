from typing import List

from extended_gcd import extended_gcd


def linear_congruence(a: int, b: int, n: int, all_solutions: bool = False) -> List[int]:
    """ 1次合同方程式 ax = b (mod n) を解く。

    Args:
        n (int): n > 1 なる整数
        a (int): 方程式のパラメータ
        b (int): 方程式のパラメータ
        all_solutions (bool): Trueならすべての解を返す

    Returns:
        List[int]: ax = b (mod n) を満たすx (0 <= x < n) のリスト
                   解なしの場合は空リスト

    Examples:
        >>> linear_congruence(3, 7, 11) # 3*6 = 7 (mod 11)
        [6]
        >>> linear_congruence(2, 9, 10) # 解なし
        []
        >>> linear_congruence(2, 4, 10) # 他にx=7も 2x = 4 (mod 10) を満たす
        [2]
        >>> linear_congruence(2, 4, 10, all_solutions=True)
        [2, 7]
    """
    g, u, _ = extended_gcd(a, n)
    if g == 1:
        return [(b * u) % n]
    if b % g != 0:
        return []
    a_, b_, n_ = a // g, b // g, n // g
    _, w, _ = extended_gcd(a_, n_)
    x = (b_ * w) % n_
    if all_solutions:
        return sorted((x + k * n_) % n for k in range(g))
    else:
        return [x]
