from homework02.tasks.hw3 import combinations


def test_assert_combinations():
    """Testing several combinations"""
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]
    assert combinations([1], [3, 4, 5]) == [[1, 3], [1, 4], [1, 5]]


if __name__ == "__main__":
    print(combinations([1, 2], [3, 4]))
    print(combinations([1], [3, 4, 5]))
