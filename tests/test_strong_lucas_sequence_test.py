from src.selfridge_method_a import selfridge_method_a
from src.sqrt_int import sqrt_int
from src.strong_lucas_sequence_test import strong_lucas_sequence_test
from sympy.ntheory import isprime


def test_strong_lucas_pseudoprimes():
    """ 強Lucas擬素数を10000未満について調べる

    Notes:
        https://oeis.org/A217255
    """
    pseudoprimes = [5459, 5777, 10877, 16109, 18971]

    for n in range(5, 20000, 2):
        if sqrt_int(n)**2 == n:
            continue
        a, b = selfridge_method_a(n)
        if a == 0 and b == 0:
            continue
        ans = strong_lucas_sequence_test(n, a, b)
        if isprime(n):
            print(n)
            assert ans == 'probable prime'
        elif n in pseudoprimes:
            assert ans == 'probable prime'
        else:
            assert ans == 'composite number'
