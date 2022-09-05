from is_square_number import is_square_number
from miller_rabin_test import miller_rabin_test
from selfridge_method_a import selfridge_method_a
from strong_lucas_sequence_test import strong_lucas_sequence_test


def baillie_psw_test(n: int) -> str:
    """ Baillie-PSWテストを用いて、nが素数かを判定する。

    Args:
        n (int): 素数判定する対象の1より大きい整数

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
    if n == 2:
        return 'prime number'
    # 底2のMiller-Rabinテスト
    if miller_rabin_test(n, a_list=[2]) == 'composite number':
        return 'composite number'
    if is_square_number(n):
        return 'composite number'
    a, b = selfridge_method_a(n)
    if a == 0 and b == 0:
        return 'composite number'
    # 強Lucasテスト
    result = strong_lucas_sequence_test(n, a, b)
    if result == 'composite number':
        return result
    if n <= 2**64:
        return 'prime number'
    else:
        return 'probable prime'
