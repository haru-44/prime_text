from src.lehman_method import lehman_method
from sympy.ntheory import isprime


def test_lehman_method_001():
    for n in range(23, 100000):
        s3 = int(n**(1/3))
        cond = True
        for i in range(2, s3+1):
            if n % i == 0:
                cond = False
                break
        if not cond:
            continue
        m = lehman_method(n)
        if m == 1:
            assert isprime(n)
        else:
            assert n % m == 0
