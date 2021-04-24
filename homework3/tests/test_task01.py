from homework3.tasks.task01 import *


def test_uncached_values():
    """Testing that only 3 values are cached"""
    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)
    val_4 = func(*some)
    assert not val_3 is val_4


def test_cached_values():
    """Testing that 3 values are cached"""
    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)
    assert val_3 is val_2 and val_2 is val_1
