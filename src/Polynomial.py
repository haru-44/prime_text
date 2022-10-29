from __future__ import annotations

from typing import List, Optional, Tuple

from inverse_mod import inverse_mod
from n_times import n_times


class Polynomial:
    """ 整数係数多項式を提供する。
    """

    def __init__(self, coef: List[int]) -> None:
        """ coefを係数とする多項式を生成する。

        Args:
            coef (List[int]): 多項式の係数。coef[i] は x^i の係数
        """
        self._coef = coef.copy()
        while len(self._coef) > 1 and self._coef[-1] == 0:
            del self._coef[-1]

    def __call__(self, x: int) -> int:
        """ 多項式にxを代入した結果を返す(Horner法による実装)。

        Args:
            x (int): 代入する整数

        Returns:
            int: 多項式にxを代入した結果

        Examples:
            >>> f = Polynomial([3, 2]) # f(x) = 3 + 2x
            >>> f(3)
            9
            >>> f(-1)
            1
        """
        y = 0
        for coef in reversed(self._coef):
            y *= x
            y += coef
        return y

    def __getitem__(self, i: int) -> int:
        """ x^i の係数を取得する。

        Args:
            i (int): x^i の係数を取得する

        Returns:
            int: x^i の係数。0 ～ deg(f) の範囲外の場合は0

        Examples:
            >>> f = Polynomial([3, 2]) # f(x) = 3 + 2x
            >>> f[0]
            3
            >>> f[2]
            0
        """
        if 0 <= i <= self.deg:
            return self._coef[i]
        else:
            return 0

    def __add__(self, other: Polynomial) -> Polynomial:
        coef = [0] * (max(self.deg, other.deg) + 1)
        for i in range(len(coef)):
            coef[i] = self[i] + other[i]
        return Polynomial(coef)

    def __sub__(self, other: Polynomial) -> Polynomial:
        coef = [0] * (max(self.deg, other.deg) + 1)
        for i in range(len(coef)):
            coef[i] = self[i] - other[i]
        return Polynomial(coef)

    def __mul__(self, other: Polynomial) -> Polynomial:
        coef = [0] * (self.deg + other.deg + 1)
        for i in range(self.deg + 1):
            for j in range(other.deg + 1):
                coef[i + j] += self[i] * other[j]
        return Polynomial(coef)

    def __rmul__(self, other: int) -> Polynomial:
        coef = [other * coef for coef in self._coef]
        return Polynomial(coef)

    def __pow__(self, other: int) -> Polynomial:
        if other == 0:
            return Polynomial([1])
        return n_times(self, other, Polynomial.__mul__)

    def __floordiv__(self, other: Polynomial) -> Polynomial:
        q, _ = Polynomial._divmod(self, other)
        return q

    def __mod__(self, other: Polynomial) -> Polynomial:
        _, r = Polynomial._divmod(self, other)
        return r

    def __eq__(self, other: Polynomial) -> bool:
        return self._coef == other._coef

    def __ne__(self, other: Polynomial) -> bool:
        return self._coef != other._coef

    @property
    def deg(self) -> int:
        """ 多項式の次数を返す。
        """
        return len(self._coef) - 1

    def is_monic(self) -> bool:
        """ 多項式がモニックかを判定する。

        (注) 最高次の係数が1の多項式をモニックと呼ぶ。
        """
        return self._coef[-1] == 1

    def is_zero(self) -> bool:
        """ 多項式がゼロかを判定する。
        """
        return self._coef == [0]

    def copy(self) -> Polynomial:
        """ この多項式のコピーを作成する。
        """
        return Polynomial(self._coef)

    def _reverse(self, d: Optional[int] = None) -> Polynomial:
        if d is None:
            d = self.deg
        return Polynomial(self._coef[d::-1])

    def _divmod(poly1: Polynomial, poly2: Polynomial) -> Tuple[Polynomial, Polynomial]:
        """ 2つの多項式の商と剰余を計算する(筆算法による実装)。

        Args:
            poly1 (Polynomial): 被除数
            poly2 (Polynomial): 除数。モニック多項式であること

        Returns:
            q, r (Polynomial, Polynomial): poly1 と poly2 の商と剰余
        """
        assert poly2.is_monic()
        q = Polynomial([0])
        r = poly1.copy()
        while not r.is_zero() and poly2.deg <= r.deg:
            t = Polynomial(([0] * (r.deg - poly2.deg)) + [r._coef[-1]])
            q += t
            r = r - t * poly2
        return q, r


class PolynomialMod:
    """ Z_nを係数とする多項式を提供する。
    """

    def __init__(self, coef: List[int], mod: int) -> None:
        """ coefを係数とする多項式を生成する。

        Args:
            coef (List[int]): 多項式の係数。coef[i] は x^i の係数
            mod (int): 剰余を取る数
        """
        self._mod = mod
        self._coef = list(c % self._mod for c in coef)
        while len(self._coef) > 1 and self._coef[-1] == 0:
            del self._coef[-1]

    def __call__(self, x: int) -> int:
        """ 多項式にxを代入した結果を返す(Horner法による実装)。

        Args:
            x (int): 代入する整数

        Returns:
            int: 多項式にxを代入した結果

        Examples:
            >>> f = PolynomialMod([3, 2], 5) # f(x) = 3 + 2x
            >>> f(3)
            4
            >>> f(-1)
            1
        """
        y = 0
        for coef in reversed(self._coef):
            y *= x
            y += coef
            y %= self._mod
        return y

    def __getitem__(self, i: int) -> int:
        """ x^i の係数を取得する。

        Args:
            i (int): x^i の係数を取得する

        Returns:
            int: x^i の係数。0 ～ deg(f) の範囲外の場合は0

        Examples:
            >>> f = PolynomialMod([8, 2], 5) # f(x) = 8 + 2x = 3 + 2x
            >>> f[0]
            3
            >>> f[2]
            0
        """
        if 0 <= i <= self.deg:
            return self._coef[i]
        else:
            return 0

    def __add__(self, other: PolynomialMod) -> PolynomialMod:
        coef = [0] * (max(self.deg, other.deg) + 1)
        for i in range(len(coef)):
            coef[i] = self[i] + other[i]
        return PolynomialMod(coef, self._mod)

    def __sub__(self, other: PolynomialMod) -> PolynomialMod:
        coef = [0] * (max(self.deg, other.deg) + 1)
        for i in range(len(coef)):
            coef[i] = self[i] - other[i]
        return PolynomialMod(coef, self._mod)

    def __mul__(self, other: PolynomialMod) -> PolynomialMod:
        coef = [0] * (self.deg + other.deg + 1)
        for i in range(self.deg + 1):
            for j in range(other.deg + 1):
                coef[i + j] += self[i] * other[j]
                coef[i + j] %= self._mod
        return PolynomialMod(coef, self._mod)

    def __rmul__(self, other: int) -> PolynomialMod:
        coef = [other * coef for coef in self._coef]
        return PolynomialMod(coef, self._mod)

    def __pow__(self, other: int) -> PolynomialMod:
        if other == 0:
            return PolynomialMod([1], self._mod)
        return n_times(self, other, PolynomialMod.__mul__)

    def __floordiv__(self, other: PolynomialMod) -> PolynomialMod:
        q, _ = PolynomialMod._divmod(self, other)
        return q

    def __mod__(self, other: PolynomialMod) -> PolynomialMod:
        _, r = PolynomialMod._divmod(self, other)
        return r

    def __eq__(self, other: PolynomialMod) -> bool:
        return self._coef == other._coef

    def __ne__(self, other: PolynomialMod) -> bool:
        return self._coef != other._coef

    @property
    def deg(self) -> int:
        """ 多項式の次数を返す。
        """
        return len(self._coef) - 1

    def is_monic(self) -> bool:
        """ 多項式がモニックかを判定する。

        (注) 最高次の係数が1の多項式をモニックと呼ぶ。
        """
        return self._coef[-1] == 1

    def is_zero(self) -> bool:
        """ 多項式がゼロかを判定する。
        """
        return self._coef == [0]

    def copy(self) -> PolynomialMod:
        """ この多項式のコピーを作成する。
        """
        return PolynomialMod(self._coef, self._mod)

    def _reverse(self, d: Optional[int] = None) -> PolynomialMod:
        if d is None:
            d = self.deg
        return PolynomialMod(self._coef[d::-1], self._mod)

    def _divmod(poly1: PolynomialMod, poly2: PolynomialMod) -> Tuple[PolynomialMod, PolynomialMod]:
        """ 2つの多項式の商と剰余を計算する(筆算法による実装)。

            poly1._mod(暗黙の内にpoly2._modと等しい)が素数のとき計算は常に成功するが、
            それ以外の場合は計算できないことがある。

        Args:
            poly1 (PolynomialMod): 被除数
            poly2 (PolynomialMod): 除数

        Returns:
            q, r (PolynomialMod, PolynomialMod): poly1 と poly2 の商と剰余

        Raises:
            ValueError: 計算できない多項式が入力されたとき
        """
        q = PolynomialMod([0], poly1._mod)
        r = poly1.copy()
        inv = inverse_mod(poly2._coef[-1], poly1._mod)
        if inv is None:
            raise ValueError()
        while not r.is_zero() and poly2.deg <= r.deg:
            t = PolynomialMod(([0] * (r.deg - poly2.deg)) +
                              [r._coef[-1] * inv], poly1._mod)
            q += t
            r = r - t * poly2
        return q, r
