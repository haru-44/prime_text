from inverse_mod import inverse_mod
from sqrt_int import sqrt_int_ceil


def baby_step_giant_step(alpha: int, beta: int, n: int) -> int | None:
    """ alpha^x = beta (mod n) を満たす x を求める。

    Examples:
        >>> baby_step_giant_step(3, 2, 5) # 3^3 = 2 (mod 5)
        3
    """
    m = sqrt_int_ceil(n)
    dic = {1: 0, alpha: 1}
    a = alpha
    for j in range(2, m):
        a = (a * alpha) % n
        dic[a] = j
    b = beta
    alpha_m = pow(inverse_mod(alpha, n), m, n)
    for i in range(m):
        if b in dic:
            return i * m + dic[b]
        b = (b * alpha_m) % n
