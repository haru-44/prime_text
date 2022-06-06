from matrix_mul import matrix_mul
from n_times import n_times


def fibonacci_sequence_matrix(n: int) -> int:
    """ Fibonacci数F_nを計算する。(行列計算を用いたバージョン)

    Args:
        n (int): n番目のFibonacci数を求める

    Returns:
        int: n番目のFibonacci数。
             ここで、F_0 = 0, F_1 = 1, F_2 = 1, ... である。

    Examples:
        >>> fibonacci_sequence_matrix(5)
        5
        >>> fibonacci_sequence_matrix(11)
        89
    """
    if n <= 1:
        return n
    f1 = [[1, 1], [1, 0]]
    return n_times(f1, n, matrix_mul)[0][1]
