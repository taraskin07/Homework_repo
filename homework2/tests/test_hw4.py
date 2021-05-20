from homework2.tasks.hw4 import *


def test_if_value_is_cached():
    """Testing whether values are cached"""
    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


if __name__ == "__main__":
    print(val_1)
    print(val_2)
