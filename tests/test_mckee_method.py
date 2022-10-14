from src.mckee_method import mckee_method
from sympy.ntheory import isprime


def test_mckee_method_001():
    for n in range(3, 5000, 2):
        flg = False
        for p in range(2, int(3*n**(1/3))):
            if n % p == 0:
                flg = True
                break
        if flg:
            continue
        if isprime(n):
            assert mckee_method(n) == 1
        else:
            ans = mckee_method(n)
            assert 1 < ans < n
            assert n % ans == 0
