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
    k = p//6 + 1
    delta1 = (3*k**2 + 3*k + 1) % p
    delta2 = 12 - (p % 6)
    k3 = pow(k, 3, p)
    coef0, coef1 = 1, 0
    for _ in range(k, p//4 + 1):
        coef0, coef1 = (coef0 * k3) % p, (coef0 + coef1 * k3) % p
        k3 = (k3 + delta1) % p
        delta1 = (delta1 + delta2) % p
        delta2 = (delta2 + 6) % p
    return coef1 == 0
