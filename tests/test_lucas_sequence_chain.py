import pytest
from src.lucas_sequence_chain import *
from src.lucas_sequence_matrix import *


@pytest.mark.parametrize(('a', 'b', 'mod'), [
    (1, -1, 5),
    (1, 2, 11),
    (3, -5, 19),
    (5, 4, 17),
])
def test_lucas_sequence_chain(a, b, mod):
    for n in range(1, 100):
        x, y = lucas_sequence_chain(n, a=a, b=b, mod=mod)
        assert lucas_sequence_matrix_v(n, a=a, b=b, mod=mod) == x
        assert lucas_sequence_matrix_v(n+1, a=a, b=b, mod=mod) == y


@pytest.mark.parametrize(('a', 'mod'), [
    (1, 5),
    (1, 11),
    (3, 19),
    (5, 17),
])
def test_lucas_sequence_chain_b(a, mod):
    for n in range(1, 50):
        for k in range(1, 5):
            x, y = lucas_sequence_chain(n, a=a, b=1, mod=mod)
            xk, xkp1 = lucas_sequence_chain_b(x, k, mod)
            assert lucas_sequence_chain(n*k, a=a, b=1, mod=mod)[0] == xk
            assert lucas_sequence_chain(n*(k+1), a=a, b=1, mod=mod)[0] == xkp1
            yk, ykp1 = lucas_sequence_chain_b(y, k, mod)
            assert lucas_sequence_chain((n+1)*k, a=a, b=1, mod=mod)[0] == yk
            assert lucas_sequence_chain((n+1)*(k+1), a=a, b=1, mod=mod)[0] == ykp1
