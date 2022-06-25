from src.totient_function import totient_function
from sympy.ntheory import totient


def test_totient_function_001():
    for n in range(1, 10000):
        assert totient_function(n) == totient(n)
