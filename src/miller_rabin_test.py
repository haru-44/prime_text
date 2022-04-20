import random

from split_int import split_int


def miller_rabin_test(n: int, k: int = 10) -> str:
    """ Miller-Rabinテストを用いて、n>2が素数かを判定する。

    計算量 : O(k |n|^3)

    Args:
        n (int): 素数判定する対象の整数
        k (int): 試行回数。既定値を10としたが、特に意味はない。
                 合成数だが'probable prime'と判定する確率は高々4^{-k}

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
    for _ in range(k):  # k回繰り返す
        a = random.randrange(2, n)  # 2 <= a < n を満たす乱数を生成する
        if pow(a, m, n) != 1 and all(pow(a, 2**t * m, n) != n - 1 for t in range(s)):
            return 'composite number'
    return 'probable prime'
