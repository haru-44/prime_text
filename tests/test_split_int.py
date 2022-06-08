from src.split_int import split_int

def test_split_int_A007814():
    """
    Notes:
        https://oeis.org/A007814
    """
    correct = [0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1,
               0, 4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2]
    for n in range(1, len(correct)+1):
        s,_ = split_int(n)
        assert correct[n-1] == s


def test_split_int_A000265():
    """
    Notes:
        https://oeis.org/A000265
    """
    correct = [1, 1, 3, 1, 5, 3, 7, 1, 9, 5, 11, 3, 13,
               7, 15, 1, 17, 9, 19, 5, 21, 11, 23, 3, 25,
               13, 27, 7]
    for n in range(1, len(correct)+1):
        _,m = split_int(n)
        assert correct[n-1] == m
