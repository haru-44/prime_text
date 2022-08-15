import math

from src.lcm import lcm


def test_lcm_001():
    for a in range(1, 50):
        for b in range(1, 50):
            assert a * b == math.gcd(a, b) * lcm(a, b)
