import math
from sympy.ntheory import n_order


def get_r_for_aks(n: int) -> int:
    """ rは、n のZ_r^*での位数がlog2(n)**2 より大きくなる最小の整数。

    Args:
        n (int): rを求める対象の自然数

    Returns:
        r (int or string): rは、ord_r(n) > log2(n)**2を満たす最小の整数
                           'composite number' : rの探索中に、nが合成数であることが判明した
    """
    minimum_order = int(math.log2(n)**2)
    for r in range(minimum_order, n):
        if math.gcd(n, r) != 1:
            return 'composite number'
        if n_order(n, r) > minimum_order:
            return r
    return n
