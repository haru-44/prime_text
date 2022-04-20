import random

from jacobi_symbol import jacobi_symbol
from legendre_symbol import legendre_symbol


def solovay_strassen_test(n: int, k: int = 10) -> str:
    """ Solovay-Strassenテストを用いて、n>2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の奇数
        k (int): 試行回数。既定値を10としたが、特に意味はない。
                 合成数だが'probable prime'と判定する確率は高々2^{-k}

    Returns:
        string: 'composite number' = nは合成数
                'probable prime'   = nはおそらく素数

    Examples:
        >>> solovay_strassen_test(101)
        'probable prime'
        >>> solovay_strassen_test(111)
        'composite number'
    """
    for _ in range(k):
        a = random.randrange(2, n)
        if jacobi_symbol(a, n) != legendre_symbol(a, n):
            return 'composite number'
    return 'probable prime'
