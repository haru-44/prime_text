from src.euler_criterion import euler_criterion


def test_euler_criterion_A175629():
    """
    Notes:
        https://oeis.org/A175629
    """
    correct = [0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1,
               0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1,
               0, 1]
    for n in range(len(correct)):
        assert euler_criterion(n, 7) == correct[n]


def test_euler_criterion_A011582():
    """
    Notes:
        https://oeis.org/A011582
    """
    correct = [0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1,
               0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1,
               0, 1, -1, 1, 1, 1, -1]
    for n in range(len(correct)):
        assert euler_criterion(n, 11) == correct[n]


def test_euler_criterion_A011583():
    """
    Notes:
        https://oeis.org/A011583
    """
    correct = [0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1,
               0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1,
               0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1]
    for n in range(len(correct)):
        assert euler_criterion(n, 13) == correct[n]


def test_euler_criterion_A165471():
    """
    Notes:
        https://oeis.org/A165471
    """
    correct = [0, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1,
               1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1,
               -1, -1]
    for n in range(len(correct)):
        assert euler_criterion(n, 65537) == correct[n]
