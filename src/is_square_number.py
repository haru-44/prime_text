from sqrt_int import sqrt_int


def is_square_number(n: int) -> bool:
    """ nが平方数かを判定する

    Args:
        n (int): 平方数かを判定する整数

    Returns:
        bool: nが平方数ならTrue。そうでなければFalse
              負数は常にFalse

    Examples:
        >>> is_square_number(26)
        False
        >>> is_square_number(36)
        True
    """
    if n < 0:
        return False
    if n <= 1:
        return True
    if n % 3 == 2:
        return False
    mod = n % 8
    if not(mod == 0 or mod == 1 or mod == 4):
        return False
    if mod == 0 and mod % 16 != 0:
        return False
    if mod == 1:
        mod5 = (n-1)//8 % 5
        if mod5 == 2 or mod5 == 4:
            return False
    if mod == 4 and (n-4) % 32 != 0:
        return False
    return sqrt_int(n)**2 == n
