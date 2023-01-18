from sympy.ntheory import primerange

from src.JacobiSignature import JacobiSignature


def test_jacobisignature_001():
    n = 101**2 * 1097
    js = JacobiSignature(n, 10)
    for _ in range(500):
        ret = js.set_value()
        if ret != 1:
            assert 1 < ret < n and n % ret == 0
            return
    assert False


def test_jacobisignature_002():
    for p in primerange(3, 100):
        for q in primerange(3, 100):
            if p == q:
                continue
            n = p**2 * q
            js = JacobiSignature(n, 10)
            while True:
                divisor = js.set_value()
                if divisor != 1:
                    break
            assert n % divisor == 0
