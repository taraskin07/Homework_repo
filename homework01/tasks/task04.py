"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    first_list_sum = []
    second_list_sum = []
    for i in a:
        for j in b:
            first_list_sum.append(j + i)

    for k in c:
        for l in d:
            second_list_sum.append(k + l)

    count = 0
    for value in first_list_sum:
        value_1 = value
        if -value_1 in second_list_sum:
            second_list_sum.remove(-value_1)
            count += 1

    return count


if __name__ == "__main__":
    A = [1, -1, 2, -2]
    B = [-1, 1, -2, 2]
    C = [-3, 3, -5, 5]
    D = [-3, 3, -5, 5]
    print(check_sum_of_four(A, B, C, D))
