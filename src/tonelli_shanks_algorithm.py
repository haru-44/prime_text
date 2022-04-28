import random
from typing import Optional

from legendre_symbol import legendre_symbol
from split_int import split_int


def tonelli_shanks_algorithm(a: int, p: int) -> Optional[int]:
    """ Tonelli-Shanksのアルゴリズム。

    x^2 = a mod p
    となるようなxを求める。
    このようなxが存在する場合、x,-xの2つが解となる。

    Args:
        a (int): 整数で、pを法として平方剰余
        p (int): 奇素数

    Returns:
        x (int or None): x^2 = a mod pを満たすxで、0～p-1の範囲の中で小さい数。
                         存在しない場合はNone

    Examples:
        >>> tonelli_shanks_algorithm(2, 7) # 4も解であるが、小さいほうの3を返す
        3
    """
    assert legendre_symbol(a, p) == 1  # aは平方非剰余であり、平方根は存在しない
    while True:  # 法pで平方非剰余なdを見つけるまでループする
        d = random.randrange(2, p)
        if legendre_symbol(d, p) == -1:
            break
    s, t = split_int(p - 1)
    A, D = pow(a, t, p), pow(d, t, p)
    mu = 0
    for i in range(s):
        if pow(A * pow(D, mu, p), pow(2, s - 1 - i), p) == p - 1:
            mu += pow(2, i)
    x = (pow(a, (t + 1) // 2, p) * pow(D, mu // 2, p)) % p
    return min(x, -x % p)
