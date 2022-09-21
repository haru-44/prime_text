from src.dirichlet_class_number_formula import *


def test_dirichlet_class_number_formula_A014602():
    """
    Notes:
        https://oeis.org/A014602
    """
    correct = [3, 4, 7, 8, 11, 19, 43, 67, 163]
    for d in correct:
        assert dirichlet_class_number_formula(-d) == 1


def test_dirichlet_class_number_formula_A014603():
    """
    Notes:
        https://oeis.org/A014603
    """
    correct = [15, 20, 24, 35, 40, 51, 52, 88, 91,
               115, 123, 148, 187, 232, 235, 267, 403, 427]
    for d in correct:
        assert dirichlet_class_number_formula(-d) == 2


def test_dirichlet_class_number_formula_A006203():
    """
    Notes:
        https://oeis.org/A006203
    """
    correct = [23, 31, 59, 83, 107, 139, 211, 283, 307,
               331, 379, 499, 547, 643, 883, 907]
    for d in correct:
        assert dirichlet_class_number_formula(-d) == 3


def test_dirichlet_class_number_formula_simplify_A014602():
    """
    Notes:
        https://oeis.org/A014602
    """
    correct = [7, 8, 11, 19, 43, 67, 163]
    for d in correct:
        assert dirichlet_class_number_formula_simplify(-d) == 1


def test_dirichlet_class_number_formula_simplify_A014603():
    """
    Notes:
        https://oeis.org/A014603
    """
    correct = [15, 20, 24, 35, 40, 51, 52, 88, 91,
               115, 123, 148, 187, 232, 235, 267, 403, 427]
    for d in correct:
        assert dirichlet_class_number_formula_simplify(-d) == 2


def test_dirichlet_class_number_formula_simplify_A006203():
    """
    Notes:
        https://oeis.org/A006203
    """
    correct = [23, 31, 59, 83, 107, 139, 211, 283, 307,
               331, 379, 499, 547, 643, 883, 907]
    for d in correct:
        assert dirichlet_class_number_formula_simplify(-d) == 3
