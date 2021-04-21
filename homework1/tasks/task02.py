"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    assert len(data) >= 3
    s1 = data[0]
    s2 = data[1]
    s3 = data[2]

    while len(data) >= 3:
        if len(data) == 3 and s1 + s2 == s3:
            return True
        elif s1 + s2 == s3:
            data = data[1:]
            s1, s2, s3 = s2, s3, data[2]
        else:
            return False
    return True


if check_fibonacci(data_to_process):
    print("it's a fib sequence!")
else:
    print("it's not a fib sequence!")
