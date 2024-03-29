from src.EllipticCurveAffine import EllipticCurveAffine


def test_EllipticCurveAffine_add_001():
    """
    Notes:
        https://graui.de/code/elliptic2/
    """
    ec = EllipticCurveAffine(a=1, b=4, p=13)
    points = [(0, 1, 0), (0, 2, 1), (0, 11, 1), (2, 1, 1), (2, 12, 1), (5, 2, 1), (5, 11, 1),
              (7, 4, 1), (7, 9, 1), (8, 2, 1), (8, 11, 1), (9, 1, 1), (9, 12, 1), (10, 0, 1)]
    table = [[(0, 1, 0), (0, 2, 1), (0, 11, 1), (2, 1, 1), (2, 12, 1), (5, 2, 1), (5, 11, 1),
              (7, 4, 1), (7, 9, 1), (8, 2, 1), (8, 11, 1), (9, 1, 1), (9, 12, 1), (10, 0, 1)],
             [(0, 2, 1), (9, 12, 1), (0, 1, 0), (8, 2, 1), (10, 0, 1), (8, 11, 1), (5, 2, 1),
              (9, 1, 1), (7, 4, 1), (5, 11, 1), (2, 12, 1), (0, 11, 1), (7, 9, 1), (2, 1, 1)],
             [(0, 11, 1), (0, 1, 0), (9, 1, 1), (10, 0, 1), (8, 11, 1), (5, 11, 1), (8, 2, 1),
              (7, 9, 1), (9, 12, 1), (2, 1, 1), (5, 2, 1), (7, 4, 1), (0, 2, 1), (2, 12, 1)],
             [(2, 1, 1), (8, 2, 1), (10, 0, 1), (9, 12, 1), (0, 1, 0), (9, 1, 1), (7, 4, 1),
              (8, 11, 1), (5, 2, 1), (7, 9, 1), (0, 11, 1), (2, 12, 1), (5, 11, 1), (0, 2, 1)],
             [(2, 12, 1), (10, 0, 1), (8, 11, 1), (0, 1, 0), (9, 1, 1), (7, 9, 1), (9, 12, 1),
              (5, 11, 1), (8, 2, 1), (0, 2, 1), (7, 4, 1), (5, 2, 1), (2, 1, 1), (0, 11, 1)],
             [(5, 2, 1), (8, 11, 1), (5, 11, 1), (9, 1, 1), (7, 9, 1), (0, 2, 1), (0, 1, 0),
              (2, 1, 1), (10, 0, 1), (0, 11, 1), (9, 12, 1), (8, 2, 1), (2, 12, 1), (7, 4, 1)],
             [(5, 11, 1), (5, 2, 1), (8, 2, 1), (7, 4, 1), (9, 12, 1), (0, 1, 0), (0, 11, 1),
              (10, 0, 1), (2, 12, 1), (9, 1, 1), (0, 2, 1), (2, 1, 1), (8, 11, 1), (7, 9, 1)],
             [(7, 4, 1), (9, 1, 1), (7, 9, 1), (8, 11, 1), (5, 11, 1), (2, 1, 1), (10, 0, 1),
              (0, 2, 1), (0, 1, 0), (2, 12, 1), (8, 2, 1), (9, 12, 1), (0, 11, 1), (5, 2, 1)],
             [(7, 9, 1), (7, 4, 1), (9, 12, 1), (5, 2, 1), (8, 2, 1), (10, 0, 1), (2, 12, 1),
              (0, 1, 0), (0, 11, 1), (8, 11, 1), (2, 1, 1), (0, 2, 1), (9, 1, 1), (5, 11, 1)],
             [(8, 2, 1), (5, 11, 1), (2, 1, 1), (7, 9, 1), (0, 2, 1), (0, 11, 1), (9, 1, 1),
              (2, 12, 1), (8, 11, 1), (7, 4, 1), (0, 1, 0), (10, 0, 1), (5, 2, 1), (9, 12, 1)],
             [(8, 11, 1), (2, 12, 1), (5, 2, 1), (0, 11, 1), (7, 4, 1), (9, 12, 1), (0, 2, 1),
              (8, 2, 1), (2, 1, 1), (0, 1, 0), (7, 9, 1), (5, 11, 1), (10, 0, 1), (9, 1, 1)],
             [(9, 1, 1), (0, 11, 1), (7, 4, 1), (2, 12, 1), (5, 2, 1), (8, 2, 1), (2, 1, 1),
              (9, 12, 1), (0, 2, 1), (10, 0, 1), (5, 11, 1), (7, 9, 1), (0, 1, 0), (8, 11, 1)],
             [(9, 12, 1), (7, 9, 1), (0, 2, 1), (5, 11, 1), (2, 1, 1), (2, 12, 1), (8, 11, 1),
              (0, 11, 1), (9, 1, 1), (5, 2, 1), (10, 0, 1), (0, 1, 0), (7, 4, 1), (8, 2, 1)],
             [(10, 0, 1), (2, 1, 1), (2, 12, 1), (0, 2, 1), (0, 11, 1), (7, 4, 1), (7, 9, 1),
              (5, 2, 1), (5, 11, 1), (9, 12, 1), (9, 1, 1), (8, 11, 1), (8, 2, 1), (0, 1, 0)]]

    for i in range(len(points)):
        for j in range(len(points)):
            assert ec.add(points[i], points[j]) == table[i][j]

