from homework1.tasks.task05 import find_maximal_subarray_sum

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


def test_example_check():
    """Testing that example list gives 16"""
    assert find_maximal_subarray_sum(nums, k) == 16


nums = []
k = 3


def test_example_check_empty():
    """Testing that empty list gives 0"""
    assert find_maximal_subarray_sum(nums, k) == 0


nums = [0, 0, 0, 0]
k = 3


def test_example_check_zero():
    """Testing that zero list gives 0"""
    assert find_maximal_subarray_sum(nums, k) == 0


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 1


def test_example_check_maximum():
    """Testing that k=1 returns maximum"""
    assert find_maximal_subarray_sum(nums, k) == max(nums)
