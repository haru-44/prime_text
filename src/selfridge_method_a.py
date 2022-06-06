from typing import Tuple

from jacobi_symbol import jacobi_symbol


def selfridge_method_a(n: int) -> Tuple[int, int]:
    """ Selfridgeの方法Aを用いて、Lucas擬素数テストの適切なパラメータを得る。

    Args:
        n (int): 平方数ではない奇数

    Returns:
        a(int), b(int): Lucas擬素数テストのためのパラメータ。
                        合成数であることが判明した場合は(0, 0)
    """
    assert n % 2 == 1
    delta = 5
    diff = -2
    while True:
        jacobi = jacobi_symbol(delta, n)
        if jacobi == -1:
            return 1, (1 - delta) // 4
        if jacobi == 0:
            return 0, 0
        delta = diff - delta
        diff *= -1
