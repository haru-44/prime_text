from src.JacobiSignature import JacobiSignature


def test_jacobisignature_001():
    n = 101**2 * 1097
    js = JacobiSignature(n, 10)
    for i in range(500):
        ret = js.set_value()
        if ret != 1:
            assert 1 < ret < n and n % ret == 0
            return
    assert False
