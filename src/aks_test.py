import math

from get_r_for_aks import get_r_for_aks
from is_perfect_power import is_perfect_power
from PolynomialCyclotomic import PolynomialCyclotomic
from totient_function import totient_function


def aks_test(n: int) -> str:
    """ AKS法によってn>=2の素数判定を行う。

    確定的アルゴリズム。

    Args:
        n (int): 素数かを判定する対象の自然数

    Returns:
        string: 'composite number' = nは合成数
                'prime number'     = nは素数

    Examples:
        >>> aks_test(31)
        'prime number'
        >>> aks_test(111)
        'composite number'
    """
    if is_perfect_power(n):
        return 'composite number'
    r = get_r_for_aks(n)
    if r == 'composite number':
        return r
    threshold = int(math.sqrt(totient_function(r)) * math.log2(n)) + 1
    if any(n % p == 0 for p in range(2, threshold)):  # thresholdまで試し割を行う
        return 'composite number'
    for a in range(1, threshold):
        # (x + a)^n と x^n + a が mod x^r - 1, n で合同でないならば合成数と判定する
        if PolynomialCyclotomic(r, n, {0: a, 1: 1})**n != \
           PolynomialCyclotomic(r, n, {0: a, n: 1}):
            return 'composite number'
    return 'prime number'
