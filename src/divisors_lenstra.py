import math
from typing import List

from inverse_mod import inverse_mod
from is_square_number import is_square_number
from sqrt_int import sqrt_int


def divisors_lenstra(n: int, s: int, r: int) -> List[int]:
    """ sを法としてrと合同なnの非自明な約数を列挙する

    制約条件 0 < r < s < n, gcd(s, r) = 1

    Examples:
        >>> divisors_lenstra(245784, 65, 1)
        [66, 196, 456, 2926, 12936]
        >>> divisors_lenstra(288288, 71, 28)
        [28, 99, 312, 2016, 4004]
    """
    assert math.gcd(s, r) == 1
    divisors_set = set()
    r_inv = inverse_mod(r, s)
    r_dash = (n * r_inv) % s
    if r > 1 and n % r == 0:  # x = 0
        divisors_set.add(r)
    if r_dash > 1 and n % r_dash == 0:  # y = 0
        divisors_set.add(n // r_dash)
    a1 = (r_inv * r_dash) % s
    if a1 == 0:
        a1 = s
    a = [s, a1]
    b = [0, 1]
    c = [0, ((n - r*r_dash)//s * r_inv) % s]
    for i in range(2, n):
        _q, _a = divmod(a[i-2], a[i-1])
        if _a == 0 and i % 2 == 1:
            _a += a[i-1]
            _q -= 1
        if _a == 0:
            break
        a.append(_a)
        b.append(b[i-2] - _q*b[i-1])
        c.append((c[i-2] - _q*c[i-1]) % s)

    tail = (n+s**2-1)//s**2 + 1
    for i in range(1, len(a)):
        if i % 2 == 0:
            c_list = [0] if c[i] == 0 else [c[i]-s, c[i]]
        else:
            st = 2*a[i]*b[i]
            rem = st % s
            st += c[i] - rem
            if c[i] < rem:
                st += s
            c_list = range(st, a[i]*b[i] + tail, s)
        for c_ in c_list:
            B = c_*s + a[i]*r + b[i]*r_dash
            delta = B**2 - 4*a[i]*b[i]*n
            if is_square_number(delta):
                sq_delta = sqrt_int(delta)
                u, v = (B + sq_delta) // 2, (B - sq_delta) // 2
                if u % a[i] == 0 and v % b[i] == 0:
                    if a[i] < u:
                        divisors_set.add(u // a[i])
                if v % a[i] == 0 and u % b[i] == 0:
                    if a[i] < v:
                        divisors_set.add(v // a[i])
    return list(sorted(divisors_set))
