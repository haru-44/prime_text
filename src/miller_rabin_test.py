import random
from typing import List

from split_int import split_int


def miller_rabin_test(n: int, k: int = 10, a_list: List[int] = None) -> str:
    """ Miller-Rabinテストを用いて、n>2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の整数
        k (int): 試行回数。既定値を10としたが、特に意味はない。
                 合成数だが'probable prime'と判定する確率は高々4^{-k}
        a_list(List[int]): 使用する底を指定する。指定した場合はkは無視される。

    Returns:
        string: 'composite number' = nは合成数
                'probable prime'   = nはおそらく素数

    Examples:
        >>> miller_rabin_test(101)
        'probable prime'
        >>> miller_rabin_test(111)
        'composite number'
    """
    s, m = split_int(n - 1)
    for a in a_list or [random.randrange(2, n) for _ in range(k)]:
        if pow(a, m, n) != 1 and all(pow(a, 2**t * m, n) != n - 1 for t in range(s)):
            return 'composite number'
    return 'probable prime'
