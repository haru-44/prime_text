from sqrt_int import sqrt_int


def trial_division(n: int, *, upper: int | None = None) -> list[int]:
    """ 試し割によって、nを素因数分解する。

    upper に整数を指定した場合、その数までを試し割する。
    従って、upper を指定した場合は完全に素因数分解されないこともある。

    Args:
        n (int): 素因数分解する対象の整数
        upper (int): 試し割を行う上限

    Returns:
        factors (list): 素因数のリスト

    Examples:
        >>> trial_division(98) # 98 = 2 * 7 * 7
        [2, 7, 7]
        >>> trial_division(98, upper=6) # 素因数が6以下についてのリストを返す
        [2]
        >>> trial_division(97) # 素因数を見つけられない場合は空リストを返す
        []
    """
    factors = []
    upper = (upper or sqrt_int(n)) + 1
    for divisor in range(2, upper):
        while n % divisor == 0:
            n //= divisor
            factors.append(divisor)
    return factors
