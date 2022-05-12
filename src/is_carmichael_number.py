from sympy.ntheory import factorint


def is_carmichael_number(n: int) -> bool:
    """ Carmichael数かを判定する

    Args:
        n (int): Carmichael数かを判定する対象の自然数

    Returns:
        bool: True = nはCarmichael数
              False = nはCarmichael数ではない

    Examples:
        >>> is_carmichael_number(1105) # 1105はCarmichael数
        True
        >>> is_carmichael_number(71) # 71は素数
        False
    """
    factor = factorint(n)
    if len(factor) == 1:
        return False
    return all(e == 1 and (n-1) % (p-1) == 0 for p, e in factor.items())
