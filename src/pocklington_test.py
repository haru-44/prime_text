import math
import random
from typing import List, Optional


def pocklington_test(n: int, qs: List[int], *,
                     k: Optional[int] = None, a_list: Optional[List[int]] = None) -> str:
    """ Pocklingtonの定理を用いて、n>2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の整数
        qs (List[int]): n-1の素因数リスト
        k (int): 試行回数の指定
        a_list(List[int]): 底の指定

    Returns:
        string: 'prime number'       = nは素数
                'composite number'   = nは合成数
                'possibly composite' = nはおそらく合成数

    Examples:
        >>> pocklington_test(97, [2], k=10)
        'prime number'
        >>> pocklington_test(100, [3, 11], k=10)
        'composite number'
    """
    F, N = 1, n - 1
    for q in qs:
        while N % q == 0:
            N //= q
            F *= q
    assert n <= F**2 # qsが条件を満たしているかチェックする
    if a_list is None:
        a_list = [random.randrange(2, n) for _ in range(k)]
    for a in a_list:
        if pow(a, n - 1, n) != 1:
            return 'composite number'
        if all(math.gcd(pow(a, (n - 1) // q, n) - 1, n) == 1 for q in qs):
            return 'prime number'
    return 'possibly composite'
