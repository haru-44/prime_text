from src.fibonacci_sequence import fibonacci_sequence


def test_fibonacci_sequence_A000045():
    """
    Notes:
        https://oeis.org/A000045
    """
    correct = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
               233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
               17711, 28657, 46368, 75025, 121393, 196418, 317811,
               514229, 832040, 1346269, 2178309, 3524578]
    for i in range(len(correct)):
        assert fibonacci_sequence(i) == correct[i]
