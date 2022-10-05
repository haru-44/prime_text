from itertools import islice

from src.continued_fraction import *

# http://oeis.org/A001333
sq2_numerators = [1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119,
                  19601, 47321, 114243, 275807, 665857, 1607521, 3880899,
                  9369319, 22619537, 54608393, 131836323, 318281039,
                  768398401, 1855077841, 4478554083, 10812186007,
                  26102926097, 63018038201, 152139002499, 367296043199]

# http://oeis.org/A000129
sq2_denominators = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741,
                    13860, 33461, 80782, 195025, 470832, 1136689, 2744210,
                    6625109, 15994428, 38613965, 93222358, 225058681,
                    543339720, 1311738121, 3166815962, 7645370045,
                    18457556052, 44560482149, 107578520350, 259717522849]


def test_continued_fraction_sqrt2():
    for i in range(1, len(sq2_numerators)):
        p, q = continued_fraction([1] + [2] * (i - 1))
        assert p == sq2_numerators[i]
        assert q == sq2_denominators[i]


def test_continued_fraction_pi():
    # http://oeis.org/A001203
    a = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2,
         2, 2, 2, 1, 84, 2, 1, 1, 15]
    # http://oeis.org/A002485
    numerators = [1, 3, 22, 333, 355, 103993, 104348, 208341, 312689,
                  833719, 1146408, 4272943, 5419351, 80143857, 165707065,
                  245850922, 411557987, 1068966896, 2549491779, 6167950454,
                  14885392687, 21053343141, 1783366216531, 3587785776203,
                  5371151992734, 8958937768937]
    # http://oeis.org/A002486
    denominators = [0, 1, 7, 106, 113, 33102, 33215, 66317, 99532, 265381,
                    364913, 1360120, 1725033, 25510582, 52746197, 78256779,
                    131002976, 340262731, 811528438, 1963319607, 4738167652,
                    6701487259, 567663097408, 1142027682075, 1709690779483,
                    2851718461558]
    for i in range(1, len(a)):
        p, q = continued_fraction(a[:i])
        assert p == numerators[i]
        assert q == denominators[i]


def test_continued_fraction_sqrt_2():
    for i, (a, p, q, Q) in enumerate(islice(continued_fraction_sqrt(2), len(sq2_numerators) - 1)):
        if i == 0:
            assert a == 1
        else:
            assert a == 2
            assert p == sq2_numerators[i + 1]
            assert q == sq2_denominators[i + 1]
            assert sq2_numerators[i]**2 - 2 * sq2_denominators[i]**2 ==\
                pow(-1, i) * Q
