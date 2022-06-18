from src.primitive_root import primitive_root
from sympy.ntheory import primerange
from sympy.ntheory.residue_ntheory import is_primitive_root


def test_primitive_root_001():
    for p in primerange(3, 1000):
        a = primitive_root(p, 1)
        assert is_primitive_root(a, p)


def test_primitive_root_002():
    for p in primerange(3, 1000):
        for e in range(2, 5):
            a = primitive_root(p, e)
            assert is_primitive_root(a, p**e)
