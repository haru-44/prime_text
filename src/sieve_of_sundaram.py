from typing import List

from sqrt_int import sqrt_int


def sieve_of_sundaram(n: int) -> List[int]:
    """ Sundaramの篩によって、2<p<=n を満たす素数pのリストを生成する

    Args:
        n (int): 生成する素数の最大値。n > 2

    Returns:
        List[int]: 3からnまでの素数リスト

    Examples:
        >>> sieve_of_sundaram(23)
        [3, 5, 7, 11, 13, 17, 19, 23]
        >>> sieve_of_sundaram(3)
        [3]
    """
    sieve_len = (n - 3) // 2 + 1
    sieve = [True] * sieve_len
    for i in range((sqrt_int(n) - 3) // 2 + 1):
        odd = 2 * i + 3
        for j in range((odd * odd - 3) // 2, sieve_len, odd):
            # この地点で odd と (2*j+3)//odd を観察すれば、
            # すべての奇数の積を走っていることが分かる。
            sieve[j] = False
    return [2 * idx + 3 for idx, is_prime in enumerate(sieve) if is_prime]
