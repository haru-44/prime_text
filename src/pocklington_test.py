import math
import random
from typing import List, Optional


def pocklington_test(n: int, qs: list[int]) -> str | None:
    """ Pocklingtonの定理を用いて、n>2が素数かを判定する。

    n-1は、FRと分解され、Fの素因数はすべて判明しているとする。
    n<=F^2 ならば素数判定が可能で、nは確実に素数(あるいは合成数)であるが、
    実行時間は運次第である。

    Args:
        n (int): 素数判定する対象の整数
        qs (list[int]): n-1の素因数リスト

    Returns:
        string: 'prime number'       = nは素数
                'composite number'   = nは合成数
                None = n-1の素因数分解が小さすぎて判別不可能

    Examples:
        >>> pocklington_test(97, [2])
        'prime number'
        >>> pocklington_test(100, [3, 11])
        'composite number'
    """
    F, N = 1, n - 1
    for q in qs:
        while N % q == 0:
            N //= q
            F *= q
    while True:
        a = random.randrange(2, n)
        if pow(a, n - 1, n) != 1:
            return 'composite number'
        if all(math.gcd(pow(a, (n - 1) // q, n) - 1, n) == 1 for q in qs):
            break
    if n <= F**2:
        return 'prime number'
