from src.peralta_method import peralta_method


def test_peralta_method_001():
    assert peralta_method(19920494599**2 * 19920494593,
                          B=500, v=1000, sigma=49) == 19920494593
