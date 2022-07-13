def euler_criterion(a: int, p: int) -> int:
    """ Eulerの規準を計算する。

    Args:
        a (int): 整数
        p (int): 奇素数。
                 仮に奇素数でない場合でも、エラーなく計算するが、結果は保証されない。

    Returns:
        int: 1  = aはpを法として平方剰余
             -1 = aはpを法として平方非剰余
             0  = aはpで割り切れる

    Examples:
        >>> euler_criterion(2, 5)
        -1
        >>> euler_criterion(4, 7)
        1
    """
    ans = pow(a, (p - 1) // 2, p)
    if ans + 1 == p:
        return -1
    return ans
