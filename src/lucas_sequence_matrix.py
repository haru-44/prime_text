from matrix_mul import matrix_mul
from n_times import n_times


def lucas_sequence_matrix_u(n: int, a: int, b: int, mod: int | None = None) -> int:
    """ Lucas数列のn番目U_nを計算する。(行列計算を用いたバージョン)

    Args:
        n (int): n番目とn+1番目のLucas数列を求める。n > 0
        a, b (int): Lucas数列のパラメータ
        mod (int): modでの剰余を求める。Noneなら剰余を計算しない。

    Returns:
        int: n番目のLucas数列の値
    """
    u1 = [[a, -b], [1, 0]]
    mat = n_times(u1, n, lambda x, y: matrix_mul(x, y, mod=mod))
    val = mat[1][0]
    if mod is None:
        return val
    else:
        return val % mod


def lucas_sequence_matrix_v(n: int, a: int, b: int, mod: int | None = None) -> int:
    """ Lucas数列のn番目V_nを計算する。(行列計算を用いたバージョン)

    Args:
        n (int): n番目とn+1番目のLucas数列を求める。n > 0
        a, b (int): Lucas数列のパラメータ
        mod (int): modでの剰余を求める。Noneなら剰余を計算しない。

    Returns:
        int: n番目のLucas数列の値
    """
    v1 = [[a, -b], [1, 0]]
    mat = n_times(v1, n, lambda x, y: matrix_mul(x, y, mod=mod))
    val = mat[1][0] * a + mat[1][1] * 2
    if mod is None:
        return val
    else:
        return val % mod
