import math

from inverse_mod import inverse_mod
from jacobi_symbol import jacobi_symbol
from lucas_sequence_v import lucas_sequence_v
from sqrt_int import sqrt_int


def quadratic_frobenius_test(n: int, a: int, b: int, method: str = 'frobenius') -> str:
    """ 2次FrobeniusテストまたはFibonacci数列テスト、Lucas数列テストを用いて、
        n > 1が素数かを判定する。

        method='frobenius'      => 2次Frobeniusテスト
        method='lucas'          => Lucas数列テスト
        method='lucas',a=1,b=-1 => Fibonacci数列テスト

    Args:
        n (int): 素数判定する対象の自然数
        a (int), b(int): パラメータ。a^2-4bは平方数でないように設定する。
        method (str): 素数判定法の種類 'frobenius' or 'lucas'

    Returns:
        str: 'probable prime'   = nはおそらく素数
             'composite number' = nは合成数

    Examples:
        >>> # 1891はFibonacci数列テストで誤って素数と判定される
        >>> quadratic_frobenius_test(n=1891, a=1, b=-1, method='lucas')
        'probable prime'
        >>> quadratic_frobenius_test(n=1891, a=1, b=-1, method='frobenius')
        'composite number'
    """
    inv_b = inverse_mod(b, n)
    if inv_b is None:  # bの逆数が存在しないならnは合成数
        return 'composite number'
    A = (a**2 * inv_b - 2) % n
    delta = a**2 - 4*b
    assert sqrt_int(delta)**2 != delta  # deltaは平方数ではない
    if math.gcd(n, 2*a*b*delta) != 1:
        return 'composite number'
    m = (n - jacobi_symbol(delta, n)) // 2
    v_m, v_mp1 = lucas_sequence_v(A, m, n)
    if (A * v_m) % n != (2 * v_mp1) % n:
        return 'composite number'
    if method == 'lucas':
        return 'probable prime'
    if (pow(b, (n-1)//2, n) * v_m) % n == 2:
        return 'probable prime'
    else:
        return 'composite number'
