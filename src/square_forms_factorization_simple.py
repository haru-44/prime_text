import math

from is_square_number import is_square_number
from sqrt_int import sqrt_int


def square_forms_factorization_simple(n: int, k: int = 1) -> int:
    """ Shanks の square forms factorization (SQUFOF) を使用して n の因数を返す。

    Args:
        n (int): 因数を求めたい整数。素数でも平方数でもないこと。
        k (int): n では解けない場合があり、小さな因数をかけると解ける可能性がある。

    Returns:
        int: n の因数。自明な因数を返す場合もある

    Examples:
        >>> square_forms_factorization_simple(11111)
        41
        >>> # 4558849 = 383 * 11903 は失敗する
        >>> square_forms_factorization_simple(4558849)
        1

    Note:
        https://en.wikipedia.org/wiki/Shanks%27s_square_forms_factorization
        を基に実装。実行上の注意は、本文を参照のこと。
    """
    n *= k
    sq = sqrt_int(n)
    P = 0
    Q, Q_prev = 1, n
    while True:
        for _ in range(2):
            a = (sq + P) // Q
            P, P_prev = a * Q - P, P
            Q, Q_prev = Q_prev + a * (P_prev - P), Q
        if is_square_number(Q):
            break
    P = -P
    Q = sqrt_int(Q)
    Q_prev *= Q
    while True:
        a = (sq + P) // Q
        P, P_prev = a * Q - P, P
        if P != P_prev:
            return math.gcd(n // k, P)
        Q, Q_prev = Q_prev + a * (P_prev - P), Q
