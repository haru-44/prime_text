class PolynomialCyclotomic():
    def __init__(self, r:int, n:int, coefs:dict={}):
        """
        Args:
            r (int): 剰余する多項式 x^r-1 のパラメータ
            n (int):
            coefs (dict): 多項式の係数。次数をキーとする。
        """
        self.r = r
        self.n = n
        self.f = [0] * r
        for coef, val in coefs.items():
            self.f[coef % r] += val % n

    def __eq__(self, other):
        assert self.r == other.r and self.n == other.n
        return self.f == other.f

    def __ne__(self, other):
        return not (self == other)

    def __mul__(self, other):
        assert self.r == other.r and self.n == other.n
        result = PolynomialCyclotomic(self.r, self.n)
        for i in range(self.r):
            for j in range(self.r):
                coef = (i + j) % self.r
                result.f[coef] += self.f[i] * other.f[j]
                result.f[coef] %= self.n
        return result

    def __pow__(self, other):
        if other == 0:
            return self.identityElement()
        if other % 2 == 0:
            return (self * self) ** (other // 2)
        else:
            return self * (self ** (other - 1))

    def identityElement(self):
        """ 乗法単位元を返す
        """
        element = PolynomialCyclotomic(self.r, self.n)
        element.f[0] = 1
        return element
