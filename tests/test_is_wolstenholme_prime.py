from src.is_wolstenholme_prime import is_wolstenholme_prime
from sympy.ntheory import primerange


def test_is_wolstenholme_prime_001():
    for p in primerange(11, 20000):
        if is_wolstenholme_prime(p):
            assert p == 16843
        else:
            assert p != 16843
