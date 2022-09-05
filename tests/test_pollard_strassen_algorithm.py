from src.pollard_strassen_algorithm import pollard_strassen_algorithm
from sympy.ntheory import isprime


def test_pollard_strassen_algorithm_001():
    for n in range(2, 1000):
        result = pollard_strassen_algorithm(n)
        if result == 1:
            assert isprime(n)
        else:
            assert n % result == 0
