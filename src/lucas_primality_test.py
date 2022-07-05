import random

from sympy import factorint


def lucas_primality_test(n: int) -> str:
    """ Lucasの定理を用いて、n > 2が素数かを判定する。

    結果を返すとき、nは確実に素数(あるいは合成数)であるが、
    実行時間は運次第である。

    Args:
        n (int): 素数判定する対象の自然数

    Returns:
        string: 'prime number'       = nは素数
                'composite number'   = nは合成数

    Examples:
        >>> lucas_primality_test(93)
        'composite number'
        >>> lucas_primality_test(101)
        'prime number'
    """
    qs = [*factorint(n - 1)]
    while True:
        a = random.randrange(2, n)
        if pow(a, n - 1, n) != 1:
            return 'composite number'
        if all(pow(a, (n - 1) // q, n) != 1 for q in qs):
            return 'prime number'
