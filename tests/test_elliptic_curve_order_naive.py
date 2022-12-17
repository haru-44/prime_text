from src.elliptic_curve_order_naive import elliptic_curve_order_naive
from src.elliptic_curve_points import elliptic_curve_points

def test_elliptic_curve_order_naive_001():
    """
    Notes:
        https://graui.de/code/elliptic2/
    """
    assert elliptic_curve_order_naive(1, 0, 13) == 20
    assert elliptic_curve_order_naive(5, 3, 19) == 25

def test_elliptic_curve_order_naive_002():
    assert elliptic_curve_order_naive(0, 4, 7) == 3
    assert elliptic_curve_order_naive(3, 1, 7) == 12
    assert elliptic_curve_order_naive(3, 0, 7) == 8
