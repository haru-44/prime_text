import bisect
import random
from typing import List

from split_int import split_int


def miller_rabin_test(n: int, k: int = 10, a_list: List[int] = None) -> str:
    """ Miller-Rabinテストを用いて、n>2が素数かを判定する。
    nが小さい場合は、既知の底を使って、確定的に素数判定を行う。

    計算量 : O(k |n|^3)

    Args:
        n (int): 素数判定する対象の整数
        k (int): 試行回数。既定値を10としたが、特に意味はない。
                 nが2^64未満なら不使用。
                 合成数だが'probable prime'と判定する確率は高々4^{-k}
        a_list(List[int]): 使用する底を指定する。指定した場合はkは無視される。

    Returns:
        string: 'composite number' = nは合成数
                'prime number'     = nは素数
                'probable prime'   = nはおそらく素数

    Examples:
        >>> miller_rabin_test(101)
        'prime number'
        >>> miller_rabin_test(111)
        'composite number'

    Notes:
        底は次のサイトから取得
        https://miller-rabin.appspot.com/
    """
    s, m = split_int(n - 1)
    deterministic_list = [(341531,             [9345883071009581737]),
                          (1050535501,         [336781006125,
                                                9639812373923155]),
                          (350269456337,       [4230279247111683200,
                                                14694767155120705706,
                                                16641139526367750375]),
                          (55245642489451,     [2,
                                                141889084524735,
                                                1199124725622454117,
                                                11096072698276303650]),
                          (7999252175582851,   [2,
                                                4130806001517,
                                                149795463772692060,
                                                186635894390467037,
                                                3967304179347715805]),
                          (585226005592931977, [2,
                                                123635709730000,
                                                9233062284813009,
                                                43835965440333360,
                                                761179012939631437,
                                                1263739024124850375]),
                          (2**64,              [2,
                                                325,
                                                9375,
                                                28178,
                                                450775,
                                                9780504,
                                                1795265022])]
    if a_list is None:
        idx = bisect.bisect([num for num, _ in deterministic_list], n)
        deterministic = idx < len(deterministic_list)
        if deterministic:
            a_list = deterministic_list[idx][1]
        else:
            a_list = [random.randrange(2, n) for _ in range(k)]
    else:
        deterministic = False
    for a in a_list:
        if pow(a, m, n) != 1 and all(pow(a, 2**t * m, n) != n - 1 for t in range(s)):
            return 'composite number'
    return 'prime number' if deterministic else 'probable prime'
