from src.quadratic_form_reduction import quadratic_form_reduction
from sympy.ntheory import divisors

"""
Notes:
    https://gist.githubusercontent.com/junpeitsuji/6c98783aee8640c4d439/raw/gistfile1.txt
"""


def test_quadratic_form_reduction_d3():
    for b in range(100):
        if (b**2 + 3) % 4 != 0:
            continue
        ac = (b**2 + 3) // 4
        for a in divisors(ac, generator=True):
            c = ac // a
            assert quadratic_form_reduction(a, b, c) == (1, 1, 1)


def test_quadratic_form_reduction_d4():
    for b in range(100):
        if (b**2 + 4) % 4 != 0:
            continue
        ac = (b**2 + 4) // 4
        for a in divisors(ac, generator=True):
            c = ac // a
            assert quadratic_form_reduction(a, b, c) == (1, 0, 1)


def test_quadratic_form_reduction_d19():
    for b in range(100):
        if (b**2 + 19) % 4 != 0:
            continue
        ac = (b**2 + 19) // 4
        for a in divisors(ac, generator=True):
            c = ac // a
            assert quadratic_form_reduction(a, b, c) == (1, 1, 5)
