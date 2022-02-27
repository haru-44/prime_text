import random


def fermat_test(n: int, *, k: int = 10) -> str:
    """ Fermatテストを用いて、n>2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の整数
        k (int): 試行回数。既定値を10としたが、特に意味はない。

    Returns:
        str: 'composite number' : nは合成数
             'probable prime'   : nはおそらく素数

    Examples:
        >>> fermat_test(2021) # 2021 = 43 * 47
        'composite number'
        >>> fermat_test(101) # 101 is prime
        'probable prime'
    """
    for _ in range(k):
        a = random.randrange(2, n)
        if pow(a, n - 1, n) != 1:
            return 'composite number'
    return 'probable prime'
