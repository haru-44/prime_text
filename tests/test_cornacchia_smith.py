from src.cornacchia_smith import *
from sympy.ntheory import primerange


def test_cornacchia_smith_001():
    for p in primerange(3, 200):
        for d in range(1, 300):
            if d % p == 0:
                continue
            result = cornacchia_smith(p, d)
            if result is None:
                for x in range(1, p):
                    for y in range(1, p):
                        r = x**2 + d * y**2
                        assert p != r
                        if r > p:
                            break
            else:
                x, y = result
                assert p == x**2 + d * y**2


def test_cornacchia_smith_4p_001():
    for p in primerange(2, 200):
        for d in range(1, 4*p):
            d = -d
            if d % 4 > 1:
                continue
            result = cornacchia_smith_4p(p, d)
            if result is None:
                for x in range(1, p):
                    for y in range(1, p):
                        r = x**2 + abs(d) * y**2
                        assert 4*p != r
                        if r > 4*p:
                            break
            else:
                x, y = result
                assert 4*p == x**2 + abs(d) * y**2