from jacobi_symbol import jacobi_symbol
from quadratic_frobenius_test import quadratic_frobenius_test
from sqrt_int import sqrt_int


def baillie_psw_test(n: int) -> str:
    """ Baillie-PSWテストを用いて、nが素数かを判定する。

    Args:
        n (int): 素数判定する対象の整数

    Returns:
        str: 'composite number' : nは合成数
             'probable prime'   : nはおそらく素数
             'prime number'     : nは素数

    Examples:
        >>> baillie_psw_test(2021) # 2021 = 43 * 47
        'composite number'
        >>> baillie_psw_test(101) # 101 is prime
        'prime number'
    """
    # 試し割は原理上不要な工程だが、小さな素因数がある合成数について
    # わざわざ以降のテストするまでもない
    for p in [2, 3, 5, 7]:
        if n % p == 0:
            return 'composite number'
    # 底2のFermatテスト
    if pow(2, n - 1, n) != 1:
        return 'composite number'
    # nが平方数の場合、次ステップで探すdeltaが見つからない
    # どのようなnを想定するかにもよるが、deltaがなかなか見つからない
    # 場合にのみチェックするなどでもよい
    if sqrt_int(n)**2 == n:
        return 'composite number'
    delta = 5
    diff = -2
    # jacobi記号(delta, n)=-1となるようなdeltaを
    # 5, -7, 9, -11, 13, ... から探す
    while jacobi_symbol(delta, n) != -1:
        delta = diff - delta
        diff *= -1
    a, b = 1, (1 - delta) // 4
    result = quadratic_frobenius_test(n, a, b, method='lucas')
    if result == 'composite number':
        return result
    if n <= 2**64:
        return 'prime number'
    else:
        return 'probable prime'
