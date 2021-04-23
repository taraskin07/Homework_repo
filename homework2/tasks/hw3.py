"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    all_combinations = []
    massive = [*args]
    from itertools import product

    for items in product(*massive):
        items = list(items)
        all_combinations.append(items)
    return all_combinations

if __name__ == "__main__":
    massive = []
    K = int(input("Enter a number of lists (K): "))
    for number_of_arrays in range(K):
        x = [
            int(i)
            for i in input(
                f"Enter a #{number_of_arrays+1} array values, separated with space: "
            ).split()
        ]
        massive.append(x)
    print(combinations(massive))
