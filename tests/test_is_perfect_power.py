from src.is_perfect_power import is_perfect_power

def test_is_perfect_power_A001597():
    """
    Notes:
        https://oeis.org/A001597
    """
    correct = [1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121,
               125, 128, 144, 169, 196, 216, 225, 243, 256, 289]
    for n in range(1, 300):
        assert (n in correct) == is_perfect_power(n)
