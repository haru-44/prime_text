from is_square_number import is_square_number
from sqrt_int import sqrt_int, sqrt_int_ceil


def fermat_factorization_method_fast(n: int) -> int:
    """ Fermat法による素因数分解を行う(高速化版)。

    Args:
        n (int): 素因数分解する正整数。2でも3でも割り切れないとする。

    Returns:
        int: nが合成数の場合は、nの非自明な約数
             nが素数の場合は、1

    Examples:
        >>> fermat_factorization_method_fast(2021) # 2021 = 43 * 47
        43
        >>> fermat_factorization_method_fast(2027) # 2027 is prime
        1
    """
    assert n > 1 and n % 2 != 0 and n % 3 != 0
    n24 = n % 24
    # 初期値と幅の設定
    st = sqrt_int_ceil(n)
    for a, diff, mod in [(11, 12, 6), (23, 12, 0),
                         (5, 6, 3), (17, 6, 3),
                         (19, 4, 2), (7, 4, 0),
                         (1, 2, 1), (13, 2, 1)]:
        if n24 == a:
            st += (mod - st) % diff
            break
    for x in range(st, (n + 9) // 6 + 1, diff):
        y2 = x**2 - n
        if is_square_number(y2):
            y = sqrt_int(y2)
            if y**2 == y2:
                return x - y
    return 1
