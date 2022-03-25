from typing import List

from sqrt_int import sqrt_int


def factor_sieve(n: int) -> List[int]:
    """ 素因数を篩う

    Args:
        n (int): nまでのリストを作成する

    Returns:
        sieve_list (list[int]): nが素数   <=> sieve_list[n] == 1
                                nが合成数 <=> sieve_list[n] == nの素因数のうち最大の自然数
    Examples:
        >>> sieve_list = factor_sieve(100)
        >>> sieve_list[20] # 20 = 2**2 * 5 の最大の素因数は5
        5
        >>> sieve_list[13] # 13 は素数
        1
        """
    sieve_list = [1] * (n + 1)
    for p in range(2, sqrt_int(n) + 1):
        if sieve_list[p] == 1:
            for idx in range(2 * p, n + 1, p):
                sieve_list[idx] = p
    return sieve_list
