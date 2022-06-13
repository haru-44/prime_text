from src.nth_root_int import nth_root_int

def test_nth_root_int_001():
    for n in range(2, 5):
        for i in range(100):
            assert i == nth_root_int(i**n, n)


def test_nth_root_int_002():
    for n in range(2, 5):
        for i in range(1, 100):
            assert i == nth_root_int(i**n+1, n)


def test_nth_root_int_003():
    for n in range(2, 5):
        for i in range(2, 100):
            assert i-1 == nth_root_int(i**n-1, n)

