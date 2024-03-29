import random

from euler_criterion import euler_criterion
from jacobi_symbol import jacobi_symbol


def solovay_strassen_test(n: int, k: int | None = None, a_list: list[int] | None = None) -> str:
    """ Solovay-Strassenテストを用いて、n>2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の奇数
        k (int): 試行回数の指定
        a_list(list[int]): 底の指定

    Returns:
        string: 'composite number' = nは合成数
                'probable prime'   = nはおそらく素数

    Examples:
        >>> solovay_strassen_test(101, a_list=[2])
        'probable prime'
        >>> solovay_strassen_test(111, a_list=[2])
        'composite number'
    """
    if a_list is None:
        a_list = [random.randrange(2, n) for _ in range(k)]
    for a in a_list:
        criterion = euler_criterion(a, n)
        if criterion == 0 or criterion != jacobi_symbol(a, n):
            return 'composite number'
    return 'probable prime'
