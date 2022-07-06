import math

from src.chainese_remainder_theorem import chainese_remainder_theorem
from src.lcm import lcm


def test_chainese_remainder_theorem_001():
    for n in range(2, 30):
        for m in range(2, 30):
            for a in range(n):
                for b in range(m):
                    ans = chainese_remainder_theorem([(a, n), (b, m)])
                    g = math.gcd(n, m)
                    if g != 1:
                        if a % g == b % g:
                            assert ans is not None
                            r, M = ans
                            assert r % n == a and r % m == b and lcm(n, m) == M
                        else:
                            assert ans is None
                    else:
                        assert ans is not None
                        r, M = ans
                        assert r % n == a and r % m == b and n*m == M


def test_chainese_remainder_theorem_002():
    for n in range(2, 30):
        for a in range(n):
            ans = chainese_remainder_theorem([(a, n)])
            assert ans is not None
            r, M = ans
            assert a == r and n == M
