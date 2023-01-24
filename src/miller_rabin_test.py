import random

from split_int import split_int


def miller_rabin_test(n: int, k: int | None = None, a_list: list[int] | None = None) -> str:
    """ Miller-Rabinテストを用いて、n>2が素数かを判定する。

    Args:
        n (int): 素数判定する対象の奇数
        k (int): 試行回数の指定
        a_list(List[int]): 底の指定

    Returns:
        string: 'composite number' = nは合成数
                'probable prime'   = nはおそらく素数

    Examples:
        >>> miller_rabin_test(101, a_list=[2])
        'probable prime'
        >>> miller_rabin_test(111, a_list=[2])
        'composite number'
    """
    if a_list is None:
        a_list = [random.randrange(2, n) for _ in range(k)]
    s, m = split_int(n - 1)
    for a in a_list:
        a = pow(a, m, n)
        if a == 1:
            continue
        is_composite = True
        for _ in range(s):
            if a == n-1:
                is_composite = False
                break
            a = pow(a, 2, n)
        if is_composite:
            return 'composite number'
    return 'probable prime'
