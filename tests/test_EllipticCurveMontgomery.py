import math

from sympy.ntheory.ecm import Point

from src.EllipticCurveMontgomery import EllipticCurveMontgomery


def test_EllipticCurveMontgomery_001():
    n = 11
    ecm = EllipticCurveMontgomery(n, 8)
    p = Point(ecm.Q[0], ecm.Q[1], ecm._a24, n)
    for k in range(1, 20):
        pk = p.mont_ladder(k)
        assert ecm.times(ecm.Q, k) == (pk.x_cord, pk.z_cord)


def test_EllipticCurveMontgomery_002():
    n = 35
    ecm = EllipticCurveMontgomery(n, 8)
    p = Point(ecm.Q[0], ecm.Q[1], ecm._a24, n)
    for k in range(1, 30):
        pk = p.mont_ladder(k)
        assert ecm.times(ecm.Q, k) == (pk.x_cord, pk.z_cord)


def test_EllipticCurveMontgomery_003():
    """
    Notes:
        Richard P. Brent, Richard E. Crandall, Karl Dilcher and C. Van Halewyn.
        "Three new factors of Fermat numbers".
        Mathematics of Computation 69(231):1297-1304, 2000
    """
    n = (2**(2**16)+1) // 825753601
    ec = EllipticCurveMontgomery(n, sigma=125546653)
    Q = ec.times(ec.Q, 2**2 * 3**2 * 7**2 * 109 *
                 761 * 2053 * 20297 * 101483 * 305419)
    assert math.gcd(Q[1], n) == 188981757975021318420037633
