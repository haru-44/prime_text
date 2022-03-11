import math


def pollard_rho_algorithm(n: int, k: int = 2, a: int = 1, s: int = 1) -> int:
    """ Pollardのρ法を用いて、nの非自明な約数を見つける。

    パラメータa, sは、1～n-1の任意の値。通常はランダムに決めて良い。
    パラメータkは、通常2を使用する。

    Args:
        n (int): 素因数分解する対象の自然数
        k, a (int): 使用するランダム関数。
                    f(x) = x^k + a
        s (int): 関数の初期値

    Returns:
        divisor (int): nの非自明な約数。発見できないときは、1

    Examples:
        >>> pollard_rho_algorithm(323) # 323 = 17 * 19
        19
    """
    u = v = s
    def _func(x):
        return (pow(x, k, n) + a) % n
    while True:
        u = _func(u)
        v = _func(_func(v))
        divisor = math.gcd(u - v, n)
        if divisor == n:
            # a, sが良くなかったか、nは素数
            return 1
        if divisor != 1:
            return divisor
