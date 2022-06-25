from src.fibonacci_sequence import fibonacci_sequence
from src.fibonacci_sequence_matrix import fibonacci_sequence_matrix


def test_fibonacci_sequence_matrix_001():
    for n in range(100):
        assert fibonacci_sequence_matrix(n) == fibonacci_sequence(n)
