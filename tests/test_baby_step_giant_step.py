import math

from src.baby_step_giant_step import baby_step_giant_step


def test_baby_step_giant_step_001():
    for n in range(3, 50):
        for alpha in range(1, n):
            if math.gcd(n, alpha) != 1:
                continue
            for x in range(n):
                beta = pow(alpha, x, n)
                ans = baby_step_giant_step(alpha, beta, n)
                assert pow(alpha, ans, n) == beta
