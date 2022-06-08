from src.legendre_symbol import legendre_symbol


def test_legendre_symbol_A175629():
    """
    Notes:
        https://oeis.org/A175629
    """
    correct = [0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1,
               0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1,
               0, 1]
    for n in range(len(correct)):
        assert legendre_symbol(n, 7) == correct[n]


def test_legendre_symbol_A011582():
    """
    Notes:
        https://oeis.org/A011582
    """
    correct = [0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1,
               0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1,
               0, 1, -1, 1, 1, 1, -1]
    for n in range(len(correct)):
        assert legendre_symbol(n, 11) == correct[n]


def test_legendre_symbol_A011583():
    """
    Notes:
        https://oeis.org/A011583
    """
    correct = [0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1,
               0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1,
               0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1]
    for n in range(len(correct)):
        assert legendre_symbol(n, 13) == correct[n]


def test_legendre_symbol_A165471():
    """
    Notes:
        https://oeis.org/A165471
    """
    correct = [0, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1,
               1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1,
               -1, -1]
    for n in range(len(correct)):
        assert legendre_symbol(n, 65537) == correct[n]
