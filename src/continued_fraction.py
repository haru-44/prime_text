from itertools import count
from typing import Generator, List, Tuple

from sqrt_int import sqrt_int


def continued_fraction(a: List[int]) -> Tuple[int, int]:
    """ 連分数 a = [a_0; a_1, a_2, ..., a_n] の有理数表示 p_n / q_n を計算する。

    Args:
        a (List[int]): 連分数 [a_0; a_1, a_2, ..., a_n]
                       len(a) > 0 であることが必要

    Returns:
        p_n, q_n (int, int): 連分数 a の有理数表示

    Examples:
        >>> continued_fraction([1, 1, 2, 1, 2])
        (19, 11)
    """
    p, p_prev = a[0], 1
    q, q_prev = 1, 0
    for i in range(1, len(a)):
        p, p_prev = p * a[i] + p_prev, p
        q, q_prev = q * a[i] + q_prev, q
    return p, q


def continued_fraction_sqrt(N: int) -> Generator[Tuple[int, int, int, int], None, None]:
    """ sqrt(D) の 連分数 [a_0; a_1, a_2, ..., a_n] および有理数近似 p_n / q_n を計算する。

    Args:
        N (int): 平方数でない正整数

    Yields:
        a_i (int): 連分数表示
        p_i, q_i (int, int): 有理数近似
        Q_i (int): p_{i-1}^2 - Nq_{i-1}^2 = (-1)^i Q_i を満たす整数

    Examples:
        >>> from itertools import islice
        >>> # sqrt(3) の連分数展開を a_4 まで求める
        >>> [a for a, *_ in islice(continued_fraction_sqrt(3), 5)]
        [1, 1, 2, 1, 2]
    """
    sq = sqrt_int(N)
    a = sq
    P = 0
    Q, Q_prev = 1, N
    p, p_prev = a, 1
    q, q_prev = 1, 0
    yield a, p, q, Q
    for i in count(1):
        P, P_prev = a * Q - P, P
        Q, Q_prev = Q_prev + a * (P_prev - P), Q
        a = (sq + P) // Q
        assert p**2 - N * q**2 == pow(-1, i) * Q
        p, p_prev = p * a + p_prev, p
        q, q_prev = q * a + q_prev, q
        yield a, p, q, Q
