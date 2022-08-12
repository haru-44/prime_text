from is_perfect_power import is_perfect_power


def pseudosquare_test(n):
    """ 擬平方数を使って素数判定を行う。

    3818929未満について、確定的に素数判定を行う。
    それ以上の判定を行いたい場合は適宜、擬平方数のテーブルを伸長すること。

    Args:
        n (int): 1より大きい奇数

    Returns:
        string: 'prime number'     = nは素数
                'composite number' = nは合成数
                'perfect power'    = nは累乗数

    Examples:
        >>> pseudosquare_test(81)
        'perfect power'
        >>> pseudosquare_test(101)
        'prime number'
        >>> pseudosquare_test(105)
        'composite number'

    Notes:
        擬平方数のテーブルは、以下の文献を参照した。
        Jonathan P. Sorenson
        "Sieving for Pseudosquares and Pseudocubes in Parallel Using Doubly-Focused Enumeration and Wheel Datastructures"
        DOI: 10.1007/978-3-642-14518-6_26
    """
    if is_perfect_power(n):
        return 'perfect power'
    t = pow(2, (n-1) // 2, n)
    if n % 8 == 5 and t != n - 1:
        return 'composite number'
    if 1 < t < n - 1:
        return 'composite number'
    flg = False
    for p, l_p in [(3, 73), (5, 241), (7, 1009), (11, 2641), (13, 8089),
                   (17, 18001), (19, 53881), (23, 87481), (29, 117049),
                   (31, 515761), (37, 1083289), (41, 3206641), (43, 3818929)]:
        t = pow(p, (n-1) // 2, n)
        if 1 < t < n - 1:
            return 'composite number'
        if t == n - 1:
            flg = True
        if n < l_p:
            break
    if n % 8 != 1 or flg:
        return 'prime number'
    else:
        return 'composite number'
