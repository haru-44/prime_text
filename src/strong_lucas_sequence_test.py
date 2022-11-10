import math

from is_square_number import is_square_number
from jacobi_symbol import jacobi_symbol
from lucas_sequence_chain import lucas_sequence_chain
from split_int import split_int


def strong_lucas_sequence_test(n: int, a: int, b: int) -> str:
    """ 強Lucas擬素数テストを用いて、n > 1が素数かを判定する。

    Args:
        n (int): 素数判定する対象の奇数
        a (int), b(int): パラメータ。a^2-4bは平方数でないように設定する。

    Returns:
        str: 'probable prime'   = nはおそらく素数
             'composite number' = nは合成数
    """
    delta = a**2 - 4*b
    if is_square_number(delta) or math.gcd(n, 2 * a * b * delta) != 1:
        raise ValueError()
    s, m = split_int(n - jacobi_symbol(delta, n))
    v_m, v_mp1 = lucas_sequence_chain(m, a, b, n)
    if v_m == 0 or (2*v_mp1 - a*v_m) % n == 0:
        return 'probable prime'
    bk = pow(b, m, n)
    for _ in range(s-1):
        v_m = (v_m**2 - 2 * bk) % n
        bk = pow(bk, 2, n)
        if v_m == 0:
            return 'probable prime'
    return 'composite number'
