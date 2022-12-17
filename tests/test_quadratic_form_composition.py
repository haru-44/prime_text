from src.n_times import n_times
from src.quadratic_form_class_number_naive import *
from src.quadratic_form_composition import *


def test_quadratic_form_composition_d3():
    f = 1, 1, 1
    assert quadratic_form_composition(*f, *f) == (1, 1, 1)


def test_quadratic_form_composition_d15():
    f = 2, 1, 2
    assert quadratic_form_composition(*f, *f) == (1, 1, 4)
    f = 1, 1, 4
    assert quadratic_form_composition(*f, *f) == (1, 1, 4)


def test_quadratic_form_composition_d23():
    f = 2, 1, 3
    g = 2, -1, 3
    assert quadratic_form_composition(*f, *g) == (1, 1, 6)
    assert n_times(f, 2, lambda x, y: quadratic_form_composition(*x, *y)) == g
    assert n_times(g, 2, lambda x, y: quadratic_form_composition(*x, *y)) == f


def test_quadratic_form_composition2_d3():
    f = 1, 1, 1
    assert quadratic_form_composition2(*f) == (1, 1, 1)


def test_quadratic_form_composition2_d15():
    f = 2, 1, 2
    assert quadratic_form_composition2(*f) == (1, 1, 4)
    f = 1, 1, 4
    assert quadratic_form_composition2(*f) == (1, 1, 4)


def test_quadratic_form_composition2_001():
    for D in list(range(-4, -200, -4)) + list(range(-3, -200, -4)):
        for a, b, c in quadratic_form_class_number_naive(D):
            assert quadratic_form_composition(
                a, b, c, a, b, c) == quadratic_form_composition2(a, b, c)


def test_quadratic_form_composition3_001():
    for D in list(range(-4, -200, -4)) + list(range(-3, -200, -4)):
        for a, b, c in quadratic_form_class_number_naive(D):
            assert quadratic_form_composition(
                a, b, c, *quadratic_form_composition2(a, b, c)) == quadratic_form_composition3(a, b, c)
