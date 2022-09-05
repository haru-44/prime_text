from typing import Iterable, Iterator, List, Optional, Union

from Polynomial import *


def multipoint_evaluation(poly: Union[Polynomial, PolynomialMod],
                          xs: Iterable[int], delta: int = 4) -> List[int]:
    """ 多項式fと (x_0, x_1, ..., x_k)に対して f(x_0), f(x_1), ..., f(x_k) を計算する。

    Args:
        poly (Polynomial or PolynomialMod): 多項式
        xs (Iterable[int]): xの列
        delta (int): 剰余計算を打ち切る次数。結果に差異はないが、計算速度に影響を与える。

    Returns:
        List[int]: f(x_0), f(x_1), ..., f(x_k) のリスト

    Examples:
        >>> # Polynomial([0, 0, 1]) <=> x^2
        >>> multipoint_evaluation(Polynomial([0, 0, 1]), range(1, 10, 2))
        [1, 9, 25, 49, 81]

    Notes:
        multipoint_evaluation_ap は等差数列が対象であることに対して multipoint_evaluation は
        任意の数列に対応している。multipoint_evaluation_ap は deg(f) << n のとき効率的なアルゴリズムであるから、
        同じ等差数列であっても多項式の次数によっては multipoint_evaluation を使った方が早い場合もある。
        もちろん、素朴な逐次評価の方が速い場合もあるので、適宜使い分けたい。
    """
    if isinstance(poly, PolynomialMod):
        gs = [PolynomialMod([-x, 1], poly._mod) for x in xs]
    else:
        gs = [Polynomial([-x, 1]) for x in xs]
    pos = 0
    while pos + 1 < len(gs):
        gs.append(gs[pos] * gs[pos + 1])
        pos += 2
    gs[pos] = poly.copy() % gs[pos]
    for pos2 in range(pos - 2, -1, -2):
        if gs[pos].deg <= delta:
            gs[pos2] = gs[pos]
            gs[pos2 + 1] = gs[pos]
        else:
            gs[pos2] = gs[pos] % gs[pos2]
            gs[pos2 + 1] = gs[pos] % gs[pos2 + 1]
        pos -= 1
    return [f(x) for x, f in zip(xs, gs[:len(xs)])]


def multipoint_evaluation_ap(poly: Union[Polynomial, PolynomialMod],
                             a: int, d: int, n: Optional[int]) -> Iterator[int]:
    """ 多項式fに対して、f(a), f(a + d), f(a + 2d), ..., f(a + (n-1)d) を順次計算する。

    Args:
        poly (Polynomial or PolynomialMod): 多項式
        n (int): Noneなら無限ループ

    Yields:
        int: f(a + kd) の値

    Examples:
        >>> # Polynomial([0, 0, 1]) <=> x^2
        >>> # よって、奇数の2乗を1から5つ出力する
        >>> list(multipoint_evaluation_ap(Polynomial([0, 0, 1]), 1, 2, 5))
        [1, 9, 25, 49, 81]

    Notes:
        multipoint_evaluation の Notes も参照のこと。
    """
    D = len(poly._coef)
    e = [poly(x) for x in range(a, a + d*D, d)]
    for q in range(1, D):
        for k in range(D - 1, q - 1, -1):
            e[k] -= e[k - 1]
    yield e[0]
    cnt = 1
    while n is None or cnt < n:
        for k in range(D - 1):
            e[k] += e[k + 1]
            if isinstance(poly, PolynomialMod):
                e[k] %= poly._mod
        yield e[0]
        cnt += 1
