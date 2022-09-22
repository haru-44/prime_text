from src.n_times import n_times
from src.quadratic_form_composition import quadratic_form_composition


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
