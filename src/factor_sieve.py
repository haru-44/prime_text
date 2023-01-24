from sqrt_int import sqrt_int


def factor_sieve(n: int) -> list[int]:
    """ 素因数を篩う

    Args:
        n (int): nまでのリストを作成する

    Returns:
        sieve_list (list[int]): nが素数   <=> sieve_list[n] == 1
                                nが合成数 <=> sieve_list[n] == nの素因数のうち最小の自然数
    Examples:
        >>> sieve_list = factor_sieve(100)
        >>> sieve_list[20] # 20 = 2**2 * 5 の最小の素因数は2
        2
        >>> sieve_list[13] # 13 は素数
        1
        """
    sieve_list = [1] * (n + 1)
    for p in range(2, sqrt_int(n) + 1):
        if sieve_list[p] == 1:
            for idx in range(2 * p, n + 1, p):
                if sieve_list[idx] == 1:
                    sieve_list[idx] = p
                else:
                    sieve_list[idx] = min(p, sieve_list[idx])
    return sieve_list
