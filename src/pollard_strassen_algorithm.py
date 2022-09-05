import functools
import math
import operator

from multipoint_evaluation import multipoint_evaluation
from Polynomial import PolynomialMod


def pollard_strassen_algorithm(n: int) -> int:
    """ Pollard-Strassen のアルゴリズムで n の非自明な約数を探索する。

    Args:
        n (int): 素因数分解する対象の自然数 n > 1

    Returns:
        int: nの非自明な約数。nが素数のときは、1

    Examples:
        >>> pollard_strassen_algorithm(323) # 323 = 17 * 19
        17
    """
    B = math.ceil(pow(n, 1/4))
    f = functools.reduce(operator.mul,
                         [PolynomialMod([-t, 1], n) for t in range(B)])
    fx = multipoint_evaluation(f, range(B, B**2 + 1, B))
    for idx, g in enumerate(map(lambda x: math.gcd(x, n), fx)):
        if g > 1:
            if g < n:
                return g
            else:
                for m in range(max(2, idx * B + 1), (idx + 1) * B + 1):
                    if n % m == 0:
                        return m
    return 1  # n is prime
