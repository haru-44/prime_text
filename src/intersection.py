from typing import Iterator, List, Tuple


def intersection(a: List[int], b: List[int]) -> Iterator[Tuple[int, int, int]]:
    """ aとbの共通部分を求める。

    Args:
        a,b: List[int]: 多重集合

    Yields:
        (int, int, int): 共通部分の元, その元のaでのインデックス, その元のbでのインデックス

    Examples:
        >>> list(intersection([3, 2, 4, 2], [1, 0, 8, 3, 3, 2])
        [(2, 1, 5), (3, 0, 3)]
    """
    a = sorted(zip(a, range(len(a))), key=lambda x: x[0])
    b = sorted(zip(b, range(len(b))), key=lambda x: x[0])
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i][0] <= b[j][0]:
            if a[i][0] == b[j][0]:
                yield a[i][0], a[i][1], b[j][1]
            i += 1
            while i < len(a) - 1 and a[i][0] == a[i-1][0]:
                i += 1
        else:
            j += 1
            while j < len(b) - 1 and b[j][0] == b[j-1][0]:
                j += 1
