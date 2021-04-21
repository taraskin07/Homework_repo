from tasks.tests import check_sum_of_four

A = [1, -1, 2, -2]
B = [-1, 1, -2, 2]
C = [-3, 3, -5, 5]
D = [-3, 3, -5, 5]

E = [1, 5, 3, -2]
F = [8, 4, -2, -7]
G = [32, 7, -5, -9]
H = [2, -4, -6, 5]

K = []
L = []
M = []
N = []


def check_that_sum_of_four_function():
    """Testing that sum of four given lists return 6"""
    assert check_sum_of_four(A, B, C, D) == 6


def check_that_sum_of_four_function_2():
    """Testing that sum of four given lists return 7"""
    assert check_sum_of_four(E, F, G, H) == 7


def check_that_sum_of_four_function_empty():
    """Testing that sum of four empty lists return 0"""
    assert check_sum_of_four(K, L, M, N) == 0
