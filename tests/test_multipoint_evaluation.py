import functools
import operator

from src.multipoint_evaluation import *
from src.Polynomial import *


def test_multipoint_evaluation_factorial001():
    for k in range(2, 10):
        poly = functools.reduce(operator.mul,
                                [Polynomial([t, 1]) for t in range(k)])
        for s in range(k, 100, k):
            assert functools.reduce(operator.mul, multipoint_evaluation(poly, range(1, s, k))) ==\
                functools.reduce(operator.mul, range(1, s + 1))


def test_multipoint_evaluation_factorial002():
    for mod in [5, 7, 11, 13]:
        for k in range(2, 10):
            poly = functools.reduce(operator.mul,
                                    [PolynomialMod([t, 1], mod) for t in range(k)])
            for s in range(k, 100, k):
                assert functools.reduce(lambda x, y: (x * y) % mod, multipoint_evaluation(poly, range(1, s, k))) ==\
                    functools.reduce(operator.mul, range(1, s + 1)) % mod


def test_multipoint_evaluation_ap_factorial001():
    for k in range(2, 10):
        poly = functools.reduce(operator.mul,
                                [Polynomial([t, 1]) for t in range(k)])
        for s in range(k, 100, k):
            assert functools.reduce(operator.mul, multipoint_evaluation_ap(poly, 1, k, s // k)) ==\
                functools.reduce(operator.mul, range(1, s + 1))


def test_multipoint_evaluation_ap_factorial002():
    for mod in [5, 7, 11, 13]:
        for k in range(2, 10):
            poly = functools.reduce(operator.mul,
                                    [PolynomialMod([t, 1], mod) for t in range(k)])
            for s in range(k, 100, k):
                assert functools.reduce(lambda x, y: (x * y) % mod, multipoint_evaluation_ap(poly, 1, k, s // k)) ==\
                    functools.reduce(operator.mul, range(1, s + 1)) % mod
