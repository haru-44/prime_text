from typing import Tuple


def lucas_sequence_chain(k: int, a: int, b: int, mod: int) -> Tuple[int, int]:
    """ Lucas数列 V_k mod n, V_{k+1} mod nを計算する。

    Args:
        a,b (int): Lucas数列Vパラメータ
        k (int): 正整数
        n (int): 正整数

    Returns:
        int, int: Lucas数列 V_k mod n と V_{k+1)} mod n の組
    """
    a, b = a % mod, b % mod
    x, y = a, (a**2 - 2*b) % mod
    bj = b
    for bit in bin(k)[3:]:
        if bit == '1':
            x, y = (x*y - a*bj) % mod, (y**2 - 2*bj*b) % mod
            bj = pow(bj, 2, mod) * b % mod
        else:
            x, y = (x**2 - 2*bj) % mod, (x*y - a*bj) % mod
            bj = pow(bj, 2, mod)
    return x, y


def lucas_sequence_chain_b(v_j: int, k: int, mod: int) -> Tuple[int, int]:
    """ Lucas数列 V_j mod nから、(V_jk mod n, V_j(k+1) mod n)を計算する。

    ここで、V_0 = 2, V_1 = a, V_j = aV_{j-1} - V_{j-2} (注: b=1)

    Args:
        v_j (int): Lucas数列のj番目
        k (int): 正整数
        n (int): 正整数

    Returns:
        int, int: jk 番目のLucas数列 V_jk mod n と V_j(k+1) mod n の組

    Examples:
        >>> # V_1 = 5, V_2 = 23, V_3 = 110, V_4 = 527
        >>> lucas_sequence_chain_b(5, 3, 100)
        (10, 27)
        >>> # (V_1 = 7,) V_2 = 47, V_3 = 322, V_4 = 2207, V_5 = 15127
        >>> # V_6 = 103682
        >>> lucas_sequence_chain_b(47, 2, 1000)
        (207, 682)
    """
    x, y = v_j, (v_j**2 - 2) % mod
    # kの2進数表記の上位ビットから下位ビットに向かって回す
    # ただし、最上位ビットの1は見ない
    for bit in bin(k)[3:]:
        if bit == '1':
            x, y = (x*y - v_j) % mod, (y**2 - 2) % mod
        else:
            x, y = (x**2 - 2) % mod, (x*y - v_j) % mod
    return x, y
