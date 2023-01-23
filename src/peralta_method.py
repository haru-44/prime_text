import math

from sympy.ntheory import primerange

from EllipticCurveMontgomery import EllipticCurveMontgomery
from inverse_mod import inverse_mod
from jacobi_symbol import jacobi_symbol


def peralta_method(n: int, B: int, v: int, sigma: int | None = None) -> int:
    """ Peralta の論文に基づく p^2q 型合成数に対する素因数分解法。

    p^2q 型合成数でなくとも実行できるが、効率は悪い。

    Args:
        n (int): gcd(n, 6) = 1
        B (int): ECM のしきい値
        v (int): 繰り返しのしきい値
        sigma (int): 楕円曲線のパラメータ。6以上の整数。指定しない場合はランダム

    Returns:
        int: n の非自明な因数。見つからない場合は1

    References:
        Rene Peralta, "Elliptic Curve Factorization Using a “Partially Oblivious” Function",
        In Cryptography and Computational Number Theory, pages 123-128, 2001
    """
    ec = EllipticCurveMontgomery(n, sigma)
    Q = ec.Q

    # ECM(Elliptic Curve Method) の stage 1
    for prime in primerange(2, B + 1):
        l = math.floor(math.log(B) / math.log(prime))
        Q = ec.times(Q, prime**l)
    assert Q[1] != 0  # Q[1] == 0 は実用上滅多に発生しないが、この場合はBが大きすぎた
    g = math.gcd(Q[1], n)
    if 1 < g < n:
        return g

    S = P = Q
    T = R = ec.double(Q)

    def _func(Q, R):
        if jacobi_symbol(Q[0], n):
            return ec.add(R, Q, P), ec.double(R)
        else:
            return ec.double(Q), ec.add(Q, R, P)

    for _ in range(v):
        Q, R = _func(Q, R)
        S, T = _func(*_func(S, T))
        d = inverse_mod(Q[1], n)
        if d is None:
            return math.gcd(Q[1], n)
        e = inverse_mod(S[1], n)
        if e is None:
            return math.gcd(S[1], n)
        g = math.gcd((Q[0] * d) - (S[0] * e), n)
        if 1 < g < n:
            return g
    return 1  # 因数を発見できなかった
