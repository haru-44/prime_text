from src.is_carmichael_number import is_carmichael_number


def test_is_carmichael_number_A002997():
    """
    Notes:
        https://oeis.org/A002997
    """
    correct = [561, 1105, 1729, 2465, 2821, 6601,
               8911, 10585, 15841, 29341, 41041,
               46657]
    for n in range(2, 50000):
        assert is_carmichael_number(n) == (n in correct)
