from src.divisors import divisors
from src.divisors_lenstra import divisors_lenstra


def test_divisors_lenstra_001():
    for n, s, r in [(245784, 65, 1), (245784, 65, 19),
                    (288288, 71, 1), (288288, 71, 28),
                    (320320, 69, 1), (320320, 69, 22),
                    (480480, 83, 5), (480480, 83, 65),
                    (911064, 115, 1), (911064, 115, 34),
                    ]:
        correct = [d for d in divisors(n) if d % s == r and d != 1 and d != n]
        pred = divisors_lenstra(n, s=s, r=r)
        assert correct == pred
