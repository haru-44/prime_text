from src.linear_congruence import linear_congruence


def test_linear_congruence_001():
    for n in range(2, 50):
        for a in range(n):
            for b in range(n):
                xs = linear_congruence(a, b, n)
                if len(xs) == 0:
                    assert all((a * x) % n != b for x in range(n))
                else:
                    assert len(xs) == 1
                    assert (a * xs[0]) % n == b


def test_linear_congruence_002():
    for n in range(2, 50):
        for a in range(n):
            for b in range(n):
                xs = linear_congruence(a, b, n, all_solutions=True)
                if len(xs) > 0:
                    for x in range(n):
                        if (a * x) % n == b:
                            assert x in xs
                        else:
                            assert x not in xs
