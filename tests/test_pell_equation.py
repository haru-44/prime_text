from src.pell_equation import pell_equation
from src.is_square_number import is_square_number

def test_pell_equation_001():
    # http://oeis.org/A033313
    xs = [3, 2, 9, 5, 8, 3, 19, 10, 7, 649, 15, 4,
          33, 17, 170, 9, 55, 197, 24, 5, 51, 26, 127,
          9801, 11, 1520, 17, 23, 35, 6, 73, 37, 25,
          19, 2049, 13, 3482, 199, 161, 24335, 48, 7,
          99, 50, 649, 66249, 485, 89, 15, 151, 19603,
          530, 31, 1766319049, 63, 8, 129, 65, 48842, 33]
    # http://oeis.org/A033317
    ys = [2, 1, 4, 2, 3, 1, 6, 3, 2, 180, 4, 1, 8, 4,
          39, 2, 12, 42, 5, 1, 10, 5, 24, 1820, 2, 273,
          3, 4, 6, 1, 12, 6, 4, 3, 320, 2, 531, 30, 24,
          3588, 7, 1, 14, 7, 90, 9100, 66, 12, 2, 20, 2574,
          69, 4, 226153980, 8, 1, 16, 8, 5967, 4, 936, 30,
          413, 2, 267000, 430, 3, 6630, 40, 6, 9]

    n = 2
    for x, y in zip(xs, ys):
        while is_square_number(n):
            n += 1
        x_, y_ = pell_equation(n)
        assert x == x_ and y == y_
        n += 1