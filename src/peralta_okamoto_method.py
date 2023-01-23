import math
import random

from sympy.ntheory import primerange

from EllipticCurveMontgomery import EllipticCurveMontgomery
from inverse_mod import inverse_mod
from JacobiSignature import JacobiSignature


def peralta_okamoto_method(n: int, B: int, k: int, sigma: int | None = None) -> int:
    """ Peralta-岡本 の論文に基づく p^2q 型合成数に対する素因数分解法。

    p^2q 型合成数でなくとも実行できるが、効率は悪い。
    因数が見つかるまでメモリを消費し続けるので適当な所で打ち切る必要がある。
    p^2q 型合成数に対するより効率的なアルゴリズムは、Peralta法を参照のこと。

    Args:
        n (int): gcd(n, 6) = 1
        B (int): ECM のしきい値
        k (int): Jacobi signature の長さ
        sigma (int): 楕円曲線のパラメータ。6以上の整数。指定しない場合はランダム

    Returns:
        int: n の非自明な因数

    References:
        Rene Peralta and Eiji Okamoto, "Faster factoring of integers of a special form",
        IEICE Trans. Fundamentals 79 (4), 489-493, 1996
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

    js = JacobiSignature(n, k)
    P = Q
    R = ec.double(Q)
    while True:
        if random.random() < 0.5:
            Q, R = ec.add(R, Q, P), ec.double(R)
        else:
            Q, R = ec.double(Q), ec.add(Q, R, P)
        d = inverse_mod(Q[1], n)
        if d is None:
            return math.gcd(Q[1], n)
        g = js.set_value((Q[0] * d) % n)
        if 1 < g < n:
            return g
