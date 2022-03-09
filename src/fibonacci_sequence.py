from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_sequence(n: int) -> int:
    """ Fibonacci数F_nを計算する。

    Args:
        n (int): n番目のFibonacci数を求める

    Returns:
        int: n番目のFibonacci数。
             ここで、F_0 = 0, F_1 = 1, F_2 = 1, ... である。

    Examples:
        >>> fibonacci_sequence(5)
        5
        >>> fibonacci_sequence(11)
        89
    """
    if n <= 1:
        return n
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
