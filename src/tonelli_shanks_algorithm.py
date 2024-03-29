from find_qnr import find_qnr
from jacobi_symbol import jacobi_symbol
from split_int import split_int


def tonelli_shanks_algorithm(a: int, p: int) -> int:
    """ Tonelli-Shanksのアルゴリズム。

    x^2 = a mod p
    となるようなxを求める。
    このようなxが存在する場合、x,-xの2つが解となる。

    Args:
        a (int): 整数で、pを法として平方剰余
        p (int): 奇素数

    Returns:
        x (int): x^2 = a mod pを満たすxで、0～p-1の範囲の中で小さい数

    Examples:
        >>> tonelli_shanks_algorithm(2, 7) # 4も解であるが、小さいほうの3を返す
        3
        >>> tonelli_shanks_algorithm(10, 13)
        6
    """
    a %= p
    # 平方剰余のときのみ、解が存在する
    if jacobi_symbol(a, p) != 1:
        raise ValueError()
    if p % 4 == 3:
        # p = 3 (mod 4) のときは、Tonelli-Shanks を使うまでもなく解ける
        x = pow(a, (p + 1) // 4, p)
    else:
        d = find_qnr(p)
        s, t = split_int(p - 1)
        A, D = pow(a, t, p), pow(d, t, p)
        m = 0
        for i in range(1, s):
            if pow(A * pow(D, m, p), pow(2, s - 1 - i), p) == p - 1:
                m += pow(2, i)
        x = (pow(a, (t + 1) // 2, p) * pow(D, m // 2, p)) % p
    return min(x, -x % p)
