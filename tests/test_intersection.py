from src.intersection import *


def test_intersection_001():
    a = [1, 2, 3]
    b = [2, 3, 4]
    ans = list(intersection(a, b))
    assert ans[0] == (2, 1, 0) and ans[1] == (3, 2, 1)


def test_intersection_dep_001():
    a = [0, 1, 0, 1]
    b = [1, 0, 1, 0]
    ans = list(intersection_dup(a, b))
    assert ans[0] == (0, [0, 2], [1, 3]) and ans[1] == (1, [1, 3], [0, 2])

def test_intersection_dup_002():
    a = [3, 2, 1]
    b = [3, 2, 1]
    ans = list(intersection_dup(a, b))
    assert ans[0] == (1, [2], [2])
    assert ans[1] == (2, [1], [1])
    assert ans[2] == (3, [0], [0])

def test_intersection_dup_003():
    a = [3, 2, 1]
    b = [3, 1, 1]
    ans = list(intersection_dup(a, b))
    assert ans[0] == (1, [2], [1, 2])
    assert ans[1] == (3, [0], [0])
