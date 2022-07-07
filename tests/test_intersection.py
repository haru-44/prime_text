from src.intersection import intersection

def test_intersection_001():
    a = [1,2,3]
    b = [2,3,4]
    ans = list(intersection(a,b))
    assert ans[0] == (2, 1, 0) and ans[1] == (3, 2, 1)
