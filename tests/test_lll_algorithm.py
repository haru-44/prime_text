from src.lll_algorithm import lll_algorithm


def test_lll_algorithm_001():
    # ref https://www.maplesoft.com/support/help/Maple/view.aspx?path=IntegerRelations%2FLLL
    assert lll_algorithm([[1, 2, 3], [1, -1, 3]]) == [[0, -3, 0], [1, -1, 3]]
    # ref https://www.youtube.com/watch?v=XEMEiBcwSKc
    assert lll_algorithm([[201, 37], [1648, 297]]) == [[1, 32], [40, 1]]
    # ref https://www.youtube.com/watch?v=n5MfVR77BTw
    assert lll_algorithm([[15, 23, 11], [46, 15, 3], [32, 1, 1]]) == [
        [1, 9, 9], [13, 5, -7], [6, -9, 15]]
    # ref https://www.youtube.com/watch?v=U8MI2a_BHHo
    assert lll_algorithm([[47, 215], [95, 460]]) == [[1, 30], [40, 5]]
    assert lll_algorithm([[1, 1, 1], [-1, 0, 2], [3, 5, 6]]
                         ) == [[0, 1, 0], [1, 0, 1], [-1, 0, 2]]


def test_lll_algorithm_approx():
    # ref https://www.youtube.com/watch?v=U8MI2a_BHHo
    alpha = 1.414213
    vec = [[1, 0, 0, 10**6],
           [0, 1, 0, int(10**6 * alpha)],
           [0, 0, 1, int(10**6 * alpha**2)]]
    assert lll_algorithm(vec) == [[-2, 0, 1, -2],
                                  [-167, -408, 372, 352],
                                  [-854, 577, 19, 863]]

    alpha = 3.105843
    vec = [[1, 0, 0, 0, 0, 0, 10**6],
           [0, 1, 0, 0, 0, 0, int(10**6 * alpha)],
           [0, 0, 1, 0, 0, 0, int(10**6 * alpha**2)],
           [0, 0, 0, 1, 0, 0, int(10**6 * alpha**3)],
           [0, 0, 0, 0, 1, 0, int(10**6 * alpha**4)],
           [0, 0, 0, 0, 0, 1, int(10**6 * alpha**5)]]
    assert lll_algorithm(vec) == [[-2, -2, 4, -2, -9, 3, -4],
                                  [-1, 1, 3, -20, 3, 1, 7],
                                  [29, -8, 14, 5, 0, -1, -15],
                                  [-1, 29, -4, -3, -12, 4, 6],
                                  [-8, -9, -19, -2, 3, 0, -31],
                                  [-28, 9, 13, 4, 16, -6, -9]]
