import math

from src.quadratic_form_class_number_naive import quadratic_form_class_number_naive
from src.quadratic_form_reduction import quadratic_form_reduction

# https://gist.githubusercontent.com/junpeitsuji/6c98783aee8640c4d439/raw/gistfile1.txt
correct_dict = {-3: 1, -4: 1, -7: 1, -8: 1, -11: 1, -12: 1, -15: 2, -16: 1, -19: 1, -20: 2,
                -23: 3, -24: 2, -27: 1, -28: 1, -31: 3, -32: 2, -35: 2, -36: 2, -39: 4, -40: 2,
                -43: 1, -44: 3, -47: 5, -48: 2, -51: 2, -52: 2, -55: 4, -56: 4, -59: 3, -60: 2,
                -63: 4, -64: 2, -67: 1, -68: 4, -71: 7, -72: 2, -75: 2, -76: 3, -79: 5, -80: 4,
                -83: 3, -84: 4, -87: 6, -88: 2, -91: 2, -92: 3, -95: 8, -96: 4, -99: 2, -100: 2,
                -103: 5, -104: 6, -107: 3, -108: 3, -111: 8, -112: 2, -115: 2, -116: 6, -119: 10,
                -120: 4, -123: 2, -124: 3, -127: 5, -128: 4, -131: 5, -132: 4, -135: 6, -136: 4,
                -139: 3, -140: 6, -143: 10, -144: 4, -147: 2, -148: 2, -151: 7, -152: 6, -155: 4,
                -156: 4, -159: 10, -160: 4, -163: 1, -164: 8, -167: 11, -168: 4, -171: 4, -172: 3,
                -175: 6, -176: 6, -179: 5, -180: 4, -183: 8, -184: 4, -187: 2, -188: 5, -191: 13,
                -192: 4, -195: 4, -196: 4, -199: 9, -200: 6}


def test_quadratic_form_class_number_naive_001():
    for D in list(range(-3, -200, -4)) + list(range(-4, -200, -4)):
        elements = list(quadratic_form_class_number_naive(D))
        assert len(elements) == correct_dict[D]
        for a, b, c in elements:
            assert b**2 - 4 * a * c == D
            assert math.gcd(math.gcd(a, b), c) == 1
            assert (a, b, c) == quadratic_form_reduction(a, b, c)
