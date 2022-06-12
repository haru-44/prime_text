from src.pepin_test import pepin_test


def test_pepin_test_001():
    for k in range(1, 5):
        assert pepin_test(k) == 'prime number'
    for k in range(5, 8):
        assert pepin_test(k) == 'composite number'
