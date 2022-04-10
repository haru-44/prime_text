import operator
from functools import reduce
from itertools import product
from typing import List

from sympy.ntheory import factorint


def divisors(n: int) -> List[int]:
    """ nの約数リストを返す

    Args:
        n (int): 対称の自然数

    Returns:
        list[int]: nの約数のリスト

    Examples:
        >>> divisors(7)
        [1, 7]
        >>> divisors(12)
        [1, 2, 3, 4, 6, 12]
    """
    factors = factorint(n)
    powers = [[pow(p, i) for i in range(e + 1)] for p, e in factors.items()]
    return sorted([reduce(operator.mul, p) for p in product(*powers)])
