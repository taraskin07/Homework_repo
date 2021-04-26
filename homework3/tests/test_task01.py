from unittest.mock import Mock

from homework3.tasks.task01 import *


@new_cache(times=3)
def func(a, b):
    return (a ** b) ** 2


# def test_uncached_values():
#     """Testing that only 3 values are cached"""
#     some = 100, 200
#
#     val_1 = func(*some)
#     val_2 = func(*some)
#     val_3 = func(*some)
#     val_4 = func(*some)
#     assert not val_3 is val_4
#
#
# def test_cached_values():
#     """Testing that 3 values are cached"""
#     some = 100, 200
#
#     val_1 = func(*some)
#     val_2 = func(*some)
#     val_3 = func(*some)
#     assert val_3 is val_2 and val_2 is val_1


def test_calls_of_func():
    func = Mock()
    some = 100, 200
    val_1 = func(*some)
    func.assert_called()
    func.assert_called_once()
    val_2 = func(*some)
    func.assert_called()
    val_3 = func(*some)
    func.assert_called()
    val_4 = func(*some)
    func.assert_called()
