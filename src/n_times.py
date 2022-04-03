from typing import Any


def n_times(a: Any, n: int, op=None) -> Any:
    """ aに対してopをn回適用する

    Args:
        a (Any): 任意のインスタンス
        n (int): 正整数
        op: a に適用する演算。デフォルトの場合、aのクラスの乗算

    Returns:
        Any: aにopをn回適用した結果

    Examples:
        >>> n_times(3, 4) # 3*3*3*3 = 3**4
        81
        >>> import operator
        >>> n_times(3, 4, operator.add) # 3+3+3+3 = 3*4
        12
        >>> n_times(3, 4, lambda x,y: (x * y) % 5) # 3**4 mod 5
        1
    """
    op = op or a.__class__.__mul__
    r = a
    n -= 1
    while n > 0:
        if n % 2 == 1:
            r = op(r, a)
        a = op(a, a)
        n >>= 1
    return r
