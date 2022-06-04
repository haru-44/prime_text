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
    def _matrix_mul(a, b):
        """ 2x2行列の積を計算する
        """
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for k in range(2):
                for j in range(2):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    if n <= 1:
        return n
    f1 = [[1, 1], [1, 0]]
    return n_times(f1, n, _matrix_mul)[0][1]
