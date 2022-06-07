import pytest
from src.lucas_sequence import *
from src.lucas_sequence_matrix import *


@pytest.mark.parametrize(('a', 'b'), [
    (1, -1),
    (1, 2),
    (3, -5),
    (5, 4),
])
@pytest.mark.parametrize('n', range(1, 100))
def test_lucas_sequence_matrix_u_z(a, b, n):
    assert lucas_sequence_u(n, a=a, b=b) == \
        lucas_sequence_matrix_u(n, a=a, b=b)


@pytest.mark.parametrize(('a', 'b', 'mod'), [
    (1, -1, 5),
    (1, 2, 11),
    (3, -5, 19),
    (5, 4, 17),
])
@pytest.mark.parametrize('n', range(1, 100))
def test_lucas_sequence_matrix_u_mod(a, b, mod, n):
    assert lucas_sequence_u(n, a=a, b=b) % mod == \
        lucas_sequence_matrix_u(n, a=a, b=b, mod=mod)


@pytest.mark.parametrize(('a', 'b'), [
    (1, -1),
    (1, 2),
    (3, -5),
    (5, 4),
])
@pytest.mark.parametrize('n', range(1, 100))
def test_lucas_sequence_matrix_v_z(a, b, n):
    assert lucas_sequence_v(n, a=a, b=b) == \
        lucas_sequence_matrix_v(n, a=a, b=b)


@pytest.mark.parametrize(('a', 'b', 'mod'), [
    (1, -1, 5),
    (1, 2, 11),
    (3, -5, 19),
    (5, 4, 17),
])
@pytest.mark.parametrize('n', range(1, 100))
def test_lucas_sequence_matrix_v_mod(a, b, mod, n):
    assert lucas_sequence_v(n, a=a, b=b) % mod == \
        lucas_sequence_matrix_v(n, a=a, b=b, mod=mod)
