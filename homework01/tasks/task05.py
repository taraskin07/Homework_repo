"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    start = 0
    stop = int(k)
    sub_array = nums[start:stop]
    total = sum(sub_array)
    maximum_sum = total
    while k > 0:
        if stop < len(nums):
            start += 1
            stop += 1
            sub_array = nums[start:stop]
            total = sum(sub_array)
            if total > maximum_sum:
                maximum_sum = total
        else:
            k -= 1
            start = 0
            stop = int(k)

    return maximum_sum


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(find_maximal_subarray_sum(nums, k))
