from src.p_minus_1_method import p_minus_1_method
from sympy.ntheory import isprime


def test_p_minus_1_method_3smooth():
    # https://oeis.org/A003586
    smooth_3 = [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27,
                32, 36, 48, 54, 64, 72, 81, 96, 108, 128,
                144, 162, 192, 216, 243, 256, 288, 324,
                384, 432, 486, 512, 576, 648, 729, 768,
                864, 972, 1024, 1152, 1296, 1458, 1536,
                1728, 1944, 2048, 2187, 2304, 2592, 2916,
                3072, 3456, 3888]
    for p in smooth_3:
        if isprime(p+1):
            f = False
            n = (p+1) * 10007
            for a in range(2, 100):
                d = p_minus_1_method(n, B=3, a=a)
                if d != 1:
                    f = True
                assert d == p+1 or d == 1
            assert f


def test_p_minus_1_method_7smooth():
    # https://oeis.org/A002473
    smooth_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12,
                14, 15, 16, 18, 20, 21, 24, 25, 27,
                28, 30, 32, 35, 36, 40, 42, 45, 48,
                49, 50, 54, 56, 60, 63, 64, 70, 72,
                75, 80, 81, 84, 90, 96, 98, 100, 105,
                108, 112, 120, 125, 126, 128, 135, 140,
                144, 147, 150, 160, 162, 168, 175, 180,
                189, 192]
    for p in smooth_7:
        if isprime(p+1):
            f = False
            n = (p+1) * 10007
            for a in range(2, 100):
                d = p_minus_1_method(n, B=7, a=a)
                if d != 1:
                    f = True
                assert d == p+1 or d == 1
            assert f
