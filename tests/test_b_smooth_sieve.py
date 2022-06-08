from src.b_smooth_sieve import b_smooth_sieve


def test_b_smooth_sieve_A003586():
    """
    Notes:
        https://oeis.org/A003586
    """
    correct = [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36,
               48, 54, 64, 72, 81, 96, 108, 128, 144, 162, 192]
    li = b_smooth_sieve(200, 3)
    for i in range(1, 200):
        assert (li[i] == i) == (i in correct)


def test_b_smooth_sieve_A002473():
    """
    Notes:
        https://oeis.org/A002473
    """
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18,
               20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 45,
               48, 49, 50, 54, 56, 60, 63, 64, 70, 72, 75, 80, 81,
               84, 90, 96, 98, 100]
    li = b_smooth_sieve(100, 7)
    for i in range(1, 101):
        assert (li[i] == i) == (i in correct)
