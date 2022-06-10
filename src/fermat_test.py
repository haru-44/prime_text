import random
from typing import List, Optional


def fermat_test(n: int, *, k: Optional[int] = None, a_list: Optional[List[int]] = None) -> str:
    """ Fermatテストを用いて、n>2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の整数
        k (int): 試行回数の指定
        a_list(List[int]): 底の指定

    Returns:
        str: 'composite number' : nは合成数
             'probable prime'   : nはおそらく素数

    Examples:
        >>> fermat_test(2021, a_list=[2]) # 2021 = 43 * 47
        'composite number'
        >>> fermat_test(101, a_list=[2]) # 101 is prime
        'probable prime'
    """
    if a_list is None:
        a_list = [random.randrange(2, n) for _ in range(k)]
    for a in a_list:
        if pow(a, n - 1, n) != 1:
            return 'composite number'
    return 'probable prime'
