from src.is_square_number import is_square_number


def test_is_square_number_A000290():
    correct = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
               121, 144, 169, 196, 225, 256, 289, 324,
               361, 400, 441, 484, 529, 576, 625, 676,
               729, 784, 841, 900, 961]

    for n in range(1000):
        assert is_square_number(n) == (n in correct)
