from typing import Any, Iterator, List, Tuple


def intersection(a: List[Any], b: List[Any]) -> Iterator[Tuple[Any, int, int]]:
    """ aとbの共通部分を求める。

    要素の重複は取り除かれる

    Args:
        a,b: List[Any]: 多重集合

    Yields:
        (Any, int, int): 共通部分の元, その元のaでのインデックス, その元のbでのインデックス

    Examples:
        >>> list(intersection([3, 2, 4, 2], [1, 0, 8, 3, 3, 2]))
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
            while i < len(a) - 1 and a[i][0] == a[i - 1][0]:
                i += 1
        else:
            j += 1
            while j < len(b) - 1 and b[j][0] == b[j - 1][0]:
                j += 1


def intersection_dup(a: List[Any], b: List[Any]) -> Iterator[Tuple[Any, List[int], List[int]]]:
    """ aとbの共通部分を求める。

    重複がある場合は、そのインデックスすべてをリストとして返す

    Args:
        a,b: List[Any]: 多重集合

    Yields:
        (Any, List[int], List[int]): 共通部分の元, その元のaでのインデックスのリスト, その元のbでのインデックスのリスト

    Examples:
        >>> list(intersection_dup([3, 2, 4, 2], [1, 0, 8, 3, 3, 2]))
        [(2, [1, 3], [5]), (3, [0], [3, 4])]
    """
    a = sorted(zip(a, range(len(a))), key=lambda x: x[0])
    b = sorted(zip(b, range(len(b))), key=lambda x: x[0])
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i][0] <= b[j][0]:
            if a[i][0] == b[j][0]:
                list_a = [a[i][1]]
                list_b = [b[j][1]]
                e = a[i][0]
                i += 1
                while i < len(a) and a[i][0] == a[i - 1][0]:
                    list_a.append(a[i][1])
                    i += 1
                j += 1
                while j < len(b) and b[j][0] == b[j - 1][0]:
                    list_b.append(b[j][1])
                    j += 1
                yield e, list_a, list_b
            else:
                i += 1
                while i < len(a) - 1 and a[i][0] == a[i - 1][0]:
                    i += 1
        else:
            j += 1
            while j < len(b) - 1 and b[j][0] == b[j - 1][0]:
                j += 1
