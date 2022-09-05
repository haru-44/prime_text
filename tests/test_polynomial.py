from src.Polynomial import *


def test_polynomial_init_001():
    assert Polynomial([1, 2, 3])._coef == [1, 2, 3]
    assert Polynomial([1, 2, 3, 0, 0])._coef == [1, 2, 3]
    assert Polynomial([1])._coef == [1]
    assert Polynomial([0])._coef == [0]


def test_polynomialmod_init_001():
    assert PolynomialMod([1, 2, 3], 5)._coef == [1, 2, 3]
    assert PolynomialMod([1, 2, 3, 0, 0], 5)._coef == [1, 2, 3]
    assert PolynomialMod([1], 5)._coef == [1]
    assert PolynomialMod([0], 5)._coef == [0]
    assert PolynomialMod([0, 5, 10], 5)._coef == [0]


def test_polynomial_call_001():
    f = Polynomial([1, 2, 3])
    for x in range(-10, 10):
        y = 3 * x**2 + 2 * x + 1
        assert f(x) == y


def test_polynomialmod_call_001():
    f = PolynomialMod([1, 2, 3], 5)
    for x in range(-10, 10):
        y = 3 * x**2 + 2 * x + 1
        assert f(x) == y % 5


def test_polynomial_divmod_001():
    f = Polynomial([1, 2, 3])
    g = Polynomial([5, 1])
    q, r = Polynomial._divmod(f, g)
    assert g.deg > r.deg and f == q * g + r


def test_polynomialmod_divmod_001():
    f = PolynomialMod([1, 2, 3], 7)
    g = PolynomialMod([5, 3], 7)
    q, r = PolynomialMod._divmod(f, g)
    assert g.deg > r.deg and f == q * g + r
