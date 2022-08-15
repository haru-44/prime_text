from src.p_minus_1_method_stage2 import p_minus_1_method_stage2


def test_p_minus_1_method_stage2_m67():
    assert p_minus_1_method_stage2(2**67 - 1, B1=67, B2=2677, a=3) == 193707721


def test_p_minus_1_method_stage2_m73():
    assert p_minus_1_method_stage2(
        (2**73 - 1) // 439, B1=73, B2=787, a=3) == 2298041


def test_p_minus_1_method_stage2_m79():
    assert p_minus_1_method_stage2(
        (2**79 - 1) // 2687, B1=79, B2=60889, a=3) == 202029703


def test_p_minus_1_method_stage2_m101():
    assert p_minus_1_method_stage2(
        2**101 - 1, B1=44029, B2=278557, a=3) == 7432339208719
