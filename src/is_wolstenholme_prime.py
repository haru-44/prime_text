def is_wolstenholme_prime(p: int) -> bool:
    """ p がWolstenholme素数かを判定する

    Args:
        p (int): 11<=p である素数

    Returns:
        bool: pがWolstenholme素数ならTrue

    Examples:
        >>> is_wolstenholme_prime(16843)
        True
        >>> is_wolstenholme_prime(11)
        False
    """
    s = p//6 + 1
    coef0, coef1 = pow(s, 3, p), 1
    for k in range(s + 1, p//4 + 1):
        k3 = pow(k, 3, p)
        coef0, coef1 = (coef0 * k3) % p, (coef0 + coef1 * k3) % p
    return coef1 == 0
