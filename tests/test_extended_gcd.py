import math

from src.extended_gcd import extended_gcd


def test_extended_gcd_001():
    for a in range(0, 100, 5):
        for b in range(0, 100, 3):
            g, x, y = extended_gcd(a, b)
            assert g == math.gcd(a, b)
            assert a*x + b*y == g


def test_extended_gcd_002():
    for a in range(0, 100, 7):
        b = a + 1
        g, x, y = extended_gcd(a, b)
        assert g == math.gcd(a, b)
        assert a*x + b*y == g
        g, x, y = extended_gcd(b, a)
        assert g == math.gcd(b, a)
        assert b*x + a*y == g
