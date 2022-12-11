"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    min = len(inp) // 2
    max = 0
    max_element = None
    min_element = None
    for element in sorted(list(set(inp))):
        if inp.count(element) >= max:
            max_element = element
            max = inp.count(element)
        if inp.count(element) <= min:
            min_element = element
            min = inp.count(element)

    return max_element, min_element


if __name__ == "__main__":
    ex1 = [3, 2, 3]
    print(major_and_minor_elem(ex1))

    ex2 = [2, 2, 1, 1, 1, 2, 2]
    print(major_and_minor_elem(ex2))
