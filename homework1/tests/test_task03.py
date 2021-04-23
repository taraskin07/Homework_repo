import os

from homework1.tasks.task03 import find_maximum_and_minimum


def test_min_and_max_in_file():
    """Testing that function return minimum -15 and maximum 566 from *.txt file"""
    abs_path = os.getcwd() + "\\homework1\\tests\\task03.txt"
    with open(
        abs_path,
        "r",
    ) as fi:
        assert find_maximum_and_minimum(fi) == (-15, 566)
