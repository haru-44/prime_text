from src.baillie_psw_test import baillie_psw_test
from sympy.ntheory import isprime


def test_baillie_psw_test():
    for n in range(2, 2**18):
        result = baillie_psw_test(n)
        if isprime(n):
            assert result == 'prime number'
        else:
            assert result == 'composite number'
