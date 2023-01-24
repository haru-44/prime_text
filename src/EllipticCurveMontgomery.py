import random

from inverse_mod import inverse_mod


class EllipticCurveMontgomery:
    """ 楕円曲線 y**2 = x**3 + C * x**2 + x の Montgomery座標を提供する。

    つまり、A=1, B=0 に限定されていることに注意する。
    Montgomery座標は (x,z) の2項組で表され、計算にも一定の制限があるが、その分速い。
    """

    def __init__(self, n: int, sigma: int | None = None) -> None:
        """ 初期化を行い、パラメータを定めると共に Q に初期点を設定する。

        楕円曲線のパラメータ C を直に指定するよりも、sigma から定まる C を使うことによって
        位数が12で割り切れるようになる。
        Q は2次ひねりの点かもしれない。

        Args:
            n (int): gcd(n,6) = 1
            sigma (int): 楕円曲線のパラメータ。6以上の整数。指定しない場合はランダム
        """
        self._n = n
        self._sigma = sigma or random.randrange(6, n)
        u = (self._sigma**2 - 5) % self._n
        v = (4 * self._sigma) % self._n
        diff = v - u
        self.Q = u_3, _ = pow(u, 3, self._n), pow(v, 3, self._n)
        C = (pow(diff, 3, n) * (3 * u + v) *
             inverse_mod(4 * u_3 * v, n) - 2) % self._n
        self._a24 = (C + 2) * inverse_mod(4, self._n) % self._n

    def add(self, P: tuple[int, int], Q: tuple[int, int], diff: tuple[int, int]) -> tuple[int, int]:
        """ Montgomery座標における加法 P+Q を計算する。ただし、diff=P-Q
        """
        P_x, P_z = P
        Q_x, Q_z = Q
        d_x, d_z = diff
        u = (P_x - P_z) * (Q_x + Q_z)
        v = (P_x + P_z) * (Q_x - Q_z)
        add, sub = u + v, u - v
        x = (d_z * add**2) % self._n
        z = (d_x * sub**2) % self._n
        return x, z

    def double(self, P: tuple[int, int]) -> tuple[int, int]:
        """ Montgomery座標におけるPの2倍を計算する。
        """
        P_x, P_z = P
        add, sub = (P_x + P_z)**2, (P_x - P_z)**2
        diff = add - sub
        x = (add * sub) % self._n
        z = (diff * (sub + self._a24 * diff)) % self._n
        return x, z

    def times(self, P: tuple[int, int], k: int) -> tuple[int, int]:
        """ Montgomery座標におけるPのk倍を計算する。
        """
        Q = P
        R = self.double(P)
        for bit in bin(k)[3:]:
            if bit == '1':
                Q, R = self.add(R, Q, P), self.double(R)
            else:
                Q, R = self.double(Q), self.add(Q, R, P)
        return Q
