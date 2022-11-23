from src.square_forms_factorization_simple import square_forms_factorization_simple


def test_square_forms_factorization_simple_001():
    """
    Notes:
        https://en.wikipedia.org/wiki/Shanks%27s_square_forms_factorization
    """
    assert square_forms_factorization_simple(11111) == 41
