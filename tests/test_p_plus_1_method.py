from src.p_plus_1_method import p_plus_1_method


def test_p_plus_1_method_m439():
    """
    Notes:
        https://www.mersenne.ca/exponent/439
    """
    # 122551752733003055543 = 2**3 * 3 * 19 * 4673 * 36037 * 13171 * 121169 + 1
    assert p_plus_1_method((2**439-1) // 104110607 //
                           127321491658223, B=121169) == 122551752733003055543


def test_p_plus_1_method_001():
    p = 207818990653657  # is prime
    for q in range(2, 20):
        n = p * (q**30 + 1)
        result = p_plus_1_method(n, B=q)
        assert result != 1 and n % result == 0
