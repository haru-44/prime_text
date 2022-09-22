from src.kronecker_symbol import kronecker_symbol


def test_kronecker_symbol_A109017():
    """
    Notes:
        https://oeis.org/A109017
    """
    correct = [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, -1,
               0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 1, 0,
               0, 0, 1, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0,
               -1, 0, -1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 1,
               0, 1, 0, 0, 0]
    for n in range(len(correct)):
        assert kronecker_symbol(-6, n) == correct[n]


def test_kronecker_symbol_A034947():
    """
    Notes:
        https://oeis.org/A034947
    """
    correct = [1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1,
               1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1,
               1, 1, -1, -1, 1]
    for n in range(len(correct)):
        assert kronecker_symbol(-1, n + 1) == correct[n]


def test_kronecker_symbol_A091337():
    """
    Notes:
        https://oeis.org/A091337
    """
    correct = [1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1,
               0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1,
               0, -1, 0, 1]
    for n in range(len(correct)):
        assert kronecker_symbol(2, n + 1) == correct[n]


def test_kronecker_symbol_A091338():
    """
    Notes:
        https://oeis.org/A091338
    """
    correct = [1, -1, 0, 1, -1, 0, -1, -1, 0, 1, 1, 0, 1,
               1, 0, 1, -1, 0, -1, -1, 0, -1, 1, 0, 1, -1,
               0, -1, -1, 0]
    for n in range(len(correct)):
        assert kronecker_symbol(3, n + 1) == correct[n]


def test_kronecker_symbol_zero():
    for a in range(2, 10):
        assert kronecker_symbol(a, 0) == 0
        assert kronecker_symbol(-a, 0) == 0
    assert kronecker_symbol(0, 0) == 0
    assert kronecker_symbol(1, 0) == 1
    assert kronecker_symbol(-1, 0) == 1

def test_kronecker_symbol_eq():
    for n in range(2, 10):
        assert kronecker_symbol(n, n) == 0
        assert kronecker_symbol(-n, -n) == 0

