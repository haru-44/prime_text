from sympy.ntheory import primerange

from src.elliptic_curve_points import elliptic_curve_points


def test_elliptic_curve_points_001():
    for p in primerange(5, 30):
        for a in range(p):
            for b in range(p):
                try:
                    itr = elliptic_curve_points(a, b, p)
                except ValueError:
                    assert (4 * a**3 + 27 * b**2) % p == 0
                s = set()
                for x, y in itr:
                    assert (x, y) not in s
                    s.add((x, y))
                    assert (x**3 + a * x + b) % p == pow(y, 2, p)
