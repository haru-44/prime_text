import math

from inverse_mod import inverse_mod
from n_times import n_times


class EllipticCurveAffine:
    def __init__(self, a: int, b: int, p: int):
        """ F_p上における楕円曲線を定義する。

        Args:
            p (int): p > 3となる整数。
            a: int, b: int: 楕円曲線のパラメータ。y**2 = x**3 + a * x + b
        """
        self.p = p
        self.a = a % p
        self.b = b % p
        if (4 * self.a**3 + 27 * self.b**2) % p == 0:
            raise ValueError()

    def _discoverd_divisor(self, d: int) -> None:
        """ pを割り切る整数dを発見したとき、例外を発生させる。

        Args:
            d (int): pを割り切る整数
        """
        raise ValueError(
            f'p is composite number. p={self.p} is divisible by {d}', d)

    def is_zero(self, P: tuple[int, int, int]) -> bool:
        """ 点Pが無限遠点かを判定する。

        Args:
            P(int, int, int): 点のx,y,z座標

        Returns:
            bool: Pが無限遠点の場合、True

        Examples:
            >>> ec = EllipticCurveAffine(3, 4, 11)
            >>> ec.is_zero((0, 1, 0)) # (0, 1, 0) は無限遠点
            True
        """
        x, y, z = P
        x %= self.p
        y %= self.p
        return x == 0 and (y == 1 or y == self.p - 1) and z == 0

    def add(self, P: tuple[int, int, int], Q: tuple[int, int, int]) -> tuple[int, int, int]:
        """ 点PとQの和を計算する。

        Args:
            P(int, int, int), Q(int, int, int): 点のx,y,z座標

        Returns:
            (int, int, int): P + Q

        Examples:
            >>> ec = EllipticCurveAffine(6, 1, 7)
            >>> ec.add((0, 1, 1), (3, 2, 1))
            (1, 1, 1)
            >>> ec.add((3, 2, 1), (3, 5, 1))
            (0, 1, 0)
        """
        if self.is_zero(P):  # P + O = P
            return Q
        if self.is_zero(Q):  # Q + O = Q
            return P
        P_x, P_y, _ = P
        Q_x, Q_y, _ = Q
        P_x, P_y = P_x % self.p, P_y % self.p
        Q_x, Q_y = Q_x % self.p, Q_y % self.p
        if P_x == Q_x:
            if (P_y + Q_y) % self.p == 0:
                return (0, 1, 0)
            inv = inverse_mod(2 * P_y, self.p)
            if inv is None:  # 逆元なし
                self._discoverd_divisor(math.gcd(2 * P_y, self.p))
            m = (3 * P_x**2 + self.a) * inv
        else:
            inv = inverse_mod(Q_x - P_x, self.p)
            if inv is None:  # 逆元なし
                self._discoverd_divisor(abs(math.gcd(Q_x - P_x, self.p)))
            m = (Q_y - P_y) * inv
        x = (m**2 - P_x - Q_x) % self.p
        y = (m * (P_x - x) - P_y) % self.p
        return (x, y, 1)

    def times(self, P: tuple[int, int, int], n: int) -> tuple[int, int, int]:
        """ Pのn倍を計算する

        Args:
            P(int, int, int): 点のx,y,z座標

        Returns:
            (int, int, int): [n]P

        Examples:
            >>> ec = EllipticCurveAffine(6, 1, 7)
            >>> ec.times((3, 2, 1), 2)
            (3, 5, 1)
            >>> ec.times((5, 4, 1), 5)
            (1, 1, 1)
        """
        return n_times(P, n, self.add)
