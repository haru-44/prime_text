from sqrt_int import sqrt_int


def sieve_of_eratosthenes(n: int) -> list[bool]:
    """ 素因数を篩う

    Args:
        n (int): nまでのリストを作成する

    Returns:
        sieve_list (list[bool]): nが素数   <=> sieve_list[n] == True
                                 nが合成数 <=> sieve_list[n] == False

    Examples:
        >>> sieve_list = sieve_of_eratosthenes(100)
        >>> sieve_list[5]
        True
        >>> sieve_list[12]
        False
    """
    sieve_list = [True] * (n + 1)
    sieve_list[0] = sieve_list[1] = False
    for p in range(2, sqrt_int(n) + 1):
        if sieve_list[p]:
            for idx in range(2 * p, n + 1, p):
                sieve_list[idx] = False
    return sieve_list
