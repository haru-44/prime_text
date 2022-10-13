import itertools
from typing import Dict, List

from chainese_remainder_theorem import chainese_remainder_theorem
from cipolla_algorithm import cipolla_algorithm
from inverse_mod import inverse_mod
from jacobi_symbol import jacobi_symbol


def sqrt_modulo_pe(a: int, p: int, e: int) -> int:
    """ x^2 = a (mod p^e) を満たす x を求める。

    Args:
        a (int): Jacobi記号(a/p)=1となるような整数。
                 なお、(a/p)=-1 のときは解なし。a=0のときは取り扱いが異なる。
        p (int): 奇素数
        e (int): 正整数

    Returns:
        x (int): x^2 = a (mod p^e) を満たすxで、0～p^e-1の範囲の中で小さい数

    Examples:
        >>> sqrt_mod_pe(3, 11, 2) # 27^2 = 3 (mod 11^2)
        27
    """
    if jacobi_symbol(a, p) != 1:
        raise ValueError()
    x = cipolla_algorithm(a, p)
    p_ = p
    z = inverse_mod(2 * x, p)
    for _ in range(e - 1):
        y = ((a - x**2) // p_) * z % p
        x += y * p_
        p_ *= p
        x %= p_
    return min(x, -x % p**e)


def sqrt_modulo_n(a: int, factors: Dict[int, int]) -> List[int]:
    """ x^2 = a (mod n) を満たす x をすべて求める。

    ただし、factorsはnの素因数分解とし、nは奇数。

    Args:
        a (int): nと互いに素な整数
        factors (Dict[int, int]): n=p_1^e_1 * p_2^e_2 * ... と素因数分解されるとき、
                                  {p_1: e_1, p_2: e_2, ...} となるような辞書型

    Returns:
        List[int]: x^2 = a (mod n) を満たすxで、0～n-1の範囲にあるすべて

    Examples:
        >>> from sympy.ntheory import factorint
        >>> sqrt_mod_n(11, factorint(35)) # 9^2 = 11 (mod 35)
        [9, 16, 19, 26]
        >>> sqrt_mod_n(3, factorint(35)) # 解なし
        []
    """
    conds = []
    for p, e in factors.items():
        if p <= 2:
            raise ValueError()
        jacobi = jacobi_symbol(a, p)
        if jacobi == 0:
            raise ValueError()
        elif jacobi == -1:  # 解なし
            return []
        x = sqrt_modulo_pe(a, p, e)
        conds.append([(x, p**e), (-x % p**e, p**e)])
    roots = []
    for exps in itertools.product(*conds):
        r, _ = chainese_remainder_theorem(exps)
        roots.append(r)
    return sorted(roots)
