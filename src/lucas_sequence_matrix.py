from typing import Tuple

from matrix_mul import matrix_mul
from n_times import n_times


def lucas_sequence_matrix(n: int, a: int, b: int, mod: int) -> Tuple[int, int]:
    """ Lucas数列のn番n+1番目V_n,V_{n+1}を計算する。(行列計算を用いたバージョン)

    Args:
        n (int): n番目とn+1番目のLucas数列を求める。n > 0
        a, b (int): Lucas数列のパラメータ

    Returns:
        (int, int): n番目とn+1番目のLucas数列の値
    """
    v1 = [[a, -b], [1, 0]]
    mat = n_times(v1, n, matrix_mul)
    return (mat[1][0] * a + mat[1][1] * 2) % mod, (mat[0][0] * a + mat[0][1] * 2) % mod
