from src.pollard_rho_algorithm import pollard_rho_algorithm


def test_pollard_rho_algorithm_001():
    """
    Notes:
        https://en.wikipedia.org/w/index.php?title=Pollard%27s_rho_algorithm&oldid=1094428495
    """
    assert pollard_rho_algorithm(8051, s=2) == 97
    assert pollard_rho_algorithm(10403, s=2) == 101


def test_pollard_rho_algorithm_002():
    """
    Notes:
        https://sofosband.wixsite.com/pversusnp/single-post/2018/08/27/factorising-part-2-pollards-rho-algorithm
    """
    assert pollard_rho_algorithm(9655379) == 2017


def test_pollard_rho_algorithm_fermat_number():
    """
    Notes:
        http://www.prothsearch.com/fermat.html
    """
    f8 = 2**(2**8) + 1
    assert pollard_rho_algorithm(f8, k=2**10, a=2) == 1238926361552897

    f10 = 2**(2**10) + 1
    k = 2**12 * 3 * 8231 * 433639 * 18840862799165386003967
    factor = k * 5639 + 1
    assert pollard_rho_algorithm(f10 // 45592577 // 6487031809,
                                 k=k, a=2) == factor
