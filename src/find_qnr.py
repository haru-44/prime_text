import random
from typing import Callable, Optional, Tuple


from jacobi_symbol import jacobi_symbol


def find_qnr(p: int, func: Callable[[int], int] = lambda x: x, random_range: Optional[Tuple[int, int]] = None) -> int:
    """ pを法とする平方非剰余を探す。

    Args:
        p (int): 奇素数
        func (callable):
        random_range (int, int): aは random_range[0] <= a < random_range[1] から選ばれる。
                                 Noneの場合は(2, p)

    Returns:
        a (int): func(a)はpを法として平方非剰余

    """
    if random_range is None:
        s, t = 2, p
    else:
        s, t = random_range
    while True:
        a = random.randrange(s, t)
        if jacobi_symbol(func(a), p) == -1:
            return a
