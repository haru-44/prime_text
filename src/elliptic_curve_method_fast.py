import math

from sympy.ntheory import primerange

from EllipticCurveMontgomery import EllipticCurveMontgomery


def elliptic_curve_method_fast(n: int, *, B1: int,  D: int,
                               B2: int | None = None,
                               sigma: int | None = None) -> int:
    """ 各種の高速化手法を取り入れた楕円曲線法を用いた素因数分解。

    Args:
        n (int): 素因数分解する整数。ただし、gcd(n,6)=1。
        B1 (int), B2(int): 第1段階、第2段階の上限で偶数。B2が設定されない場合はB2=100*B1とする。
        D (int): キャッシュサイズ。大きい程メモリを使う
        sigma (int): 楕円曲線のパラメータ。6以上の整数。指定しない場合はランダム

    Returns:
        int: nの非自明な約数
             失敗した場合は、1

    Examples:
        >>> elliptic_curve_method_fast(1000037 * 1000253, B1=20, B2=200, D=100, sigma=40)
        1000253
    """
    def _sequence(*, s_1, delta, k=None, s_0=None, s_2=None):
        """ s_1, s_2, ..., s_k を返す
        ただし、s_0 = s_1 - delta, s_1 = s_1, s_2 = s_1 + delta, s_3 = s_1 + 2delta
        """
        def _next(pre, current):
            return current, ec.add(current, delta, pre)
        yield s_1
        pre, current = _next(s_0, s_1) if s_0 is not None else (s_1, s_2)
        yield current
        k = k or B2  # k is None の場合は十分大きな値を設定する
        for _ in range(2, k):
            pre, current = _next(pre, current)
            yield current

    B2 = B2 or 100 * B1
    ec = EllipticCurveMontgomery(n, sigma)
    Q = ec.Q

    # stage 1
    for prime in primerange(2, B1 + 1):
        l = math.floor(math.log(B1) / math.log(prime))
        Q = ec.times(Q, prime**l)
    assert Q[1] != 0  # Q[1] == 0 は実用上滅多に発生しないが、この場合はB1が大きすぎた
    g = math.gcd(Q[1], n)
    if 1 < g < n:
        return g

    # stage 2
    s_1 = ec.double(Q)
    # S_i = [2(i+1)]Q
    S = list(_sequence(s_1=s_1, s_2=ec.double(s_1), delta=s_1, k=D))
    beta = [(x * z) % n for x, z in S]
    g = 1
    B = B1 - 1
    seq = _sequence(s_0=ec.times(Q, B - 2 * D),
                    s_1=ec.times(Q, B), delta=S[D-1])
    for r in range(B, B2, 2 * D):
        R_x, R_z = next(seq)
        alpha = (R_x * R_z) % n
        for q in primerange(r + 2, r + 2 * D + 1):
            delta = (q - r) // 2 - 1
            d_x, d_z = S[delta]
            f = (R_x - d_x) * (R_z + d_z) - alpha + beta[delta]
            g = (g * f) % n
    g = math.gcd(g, n)
    if 1 < g < n:
        return g
    else:
        return 1  # 失敗
