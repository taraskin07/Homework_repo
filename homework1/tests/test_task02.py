from homework1.tasks.task02 import check_fibonacci

data_to_process_pos = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]

data_to_process_neg = [
    0,
    1,
    1,
    5,
    8,
    12,
    17,
]


def test_that_fibonacci_sequence_is_fibonacci():
    """Testing that fibonacci sequence give True"""

    assert check_fibonacci(data_to_process_pos)


def test_that_random_sequence_is_not_fibonacci():
    """Testing that random sequence give False"""

    assert not check_fibonacci(data_to_process_neg)
