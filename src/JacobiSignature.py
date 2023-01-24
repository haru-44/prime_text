import math
import random

from jacobi_symbol import jacobi_symbol


class JacobiSignature:
    """ n = p^2 q 型の合成数について素因数分解を行う。

    単体でも実行可能だが O(sqrt(q)) かかることが期待され、Pollardのρ法に劣る。
    元論文のように、ECM(楕円曲線法)の後段に実行する「部品」とすることによって、
    他手法に対して優位性を持つ。

    Notes:
        Rene Peralta and Eiji Okamoto. "Faster factoring of integers of a special form",
            IEICE Transactions on Fundamentals of Electronics, Communications, and Computer Sciences,
            Vol.E79-A, No.4, pp.489-493, 1996
    """

    def __init__(self, n: int, k: int) -> None:
        """ 初期化

        Args:
            n (int): 素因数分解を行う p^2 q 型の合成数
            k (int): Jacobi signature の長さ
        """
        self._n = n
        self._k = k
        self._dic = {}

    def set_value(self, x: int | None = None) -> int:
        """ Z_n^* の元を追加し、発見した場合は n の因数を返す

        Args:
            x (int): Z_n^* の元を指定する。None の場合はランダム

        Returns:
            int: n の非自明な因数。見つからない場合は 1
        """
        x = x or random.randrange(2, self._n)
        # Jacobi signature を計算する
        sig = tuple(jacobi_symbol(x + i, self._n) for i in range(1, self._k + 1))
        if sig in self._dic:
            g = math.gcd(self._dic[sig] - x, self._n)
            if 1 < g < self._n:
                return g
        else:
            self._dic[sig] = x
        return 1
