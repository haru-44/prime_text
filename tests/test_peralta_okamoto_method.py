from src.peralta_okamoto_method import peralta_okamoto_method


def test_peralta_okamoto_method_001():
    assert peralta_okamoto_method(
        19920494599**2 * 19920494593, B=500, k=20, sigma=49) == 19920494593
