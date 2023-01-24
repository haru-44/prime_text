from copy import copy, deepcopy
from fractions import Fraction


def lll_algorithm(basis: list[list[int]], delta: float = 3/4) -> list[list[int]]:
    """ LLL アルゴリズム で基底を簡約する。

    Args:
        basis (list(list(int))): 基底
        delta (float): 1/4 < delta < 1 なる実数で、小さい程速く終わるが近似精度は悪い

    Returns:
        list(list(int)): delta-LLL 簡約基底

    Examples:
        >>> lll_algorithm([[1, 1, 1], [-1, 0, 2], [3, 5, 6]])
        [[0, 1, 0], [1, 0, 1], [-1, 0, 2]]
        >>> lll_algorithm([[1, 2, 3], [1, -1, 3]])
        [[0, -3, 0], [1, -1, 3]]
    """
    def _inner_product(a, b):
        return sum(x * y for x, y in zip(a, b))

    def _norm2(a):
        return _inner_product(a, a)

    def _mu(a, b):
        return Fraction(_inner_product(a, b), _norm2(b))

    basis = deepcopy(basis)
    n = len(basis)
    b_star = []
    k = 1
    while k < n:
        # Gram-Schmidt
        for i in range(len(b_star), k + 1):
            u_i = copy(basis[i])
            for u_j in b_star:
                s = _mu(basis[i], u_j)
                for m in range(len(u_i)):
                    u_i[m] -= s * u_j[m]
            b_star.append(u_i)
        # reduction
        for j in range(k - 1, -1, -1):
            mu_kj = _mu(basis[k], b_star[j])
            if Fraction(1, 2) < abs(mu_kj):
                r = round(mu_kj)
                for m in range(len(basis[k])):
                    basis[k][m] -= basis[j][m] * r
        # swap
        if _norm2(b_star[k]) < (delta - _mu(basis[k], b_star[k - 1])**2) * _norm2(b_star[k - 1]):
            basis[k], basis[k - 1] = basis[k - 1], basis[k]
            del b_star[k - 1:]
            k = max(k - 1, 1)
        else:
            k += 1
    return basis
