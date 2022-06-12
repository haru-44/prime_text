import random
from typing import List, Optional

from jacobi_symbol import jacobi_symbol


def proth_test(s: int, m: int, *,
               k: Optional[int] = None,
               a_list: Optional[List[int]] = None) -> str:
    """ Prothテストを用いて、n = m * 2**s + 1が素数かを判定する。

    Args:
        s (int): m < 2**s を満たす
        m (int): 奇数
        k (int): 試行回数の指定
        a_list(List[int]): 底の指定

    Returns:
        string: 'prime number'       = nは素数
                'composite number'   = nは合成数
                'possibly composite' = nはおそらく合成数

    Examples:
        >>> proth_test(3, 5, k=10) # 5 * 2**3 + 1 = 41 is prime
        'prime number'
        >>> proth_test(8, 5, k=10) # 5 * 2**8 + 1 = 1281 is composite
        'composite number'
        >>> proth_test(4, 3, k=10) # 3 * 2**4 + 1 = 49 is composite
        'possibly composite'
    """
    n = m * 2**s + 1
    if a_list is None:
        a_list = [random.randrange(2, n) for _ in range(k)]
    for a in a_list:
        if jacobi_symbol(a, n) == -1:
            if pow(a, (n - 1) // 2, n) == n - 1:
                return 'prime number'
            else:
                return 'composite number'
    return 'possibly composite'
