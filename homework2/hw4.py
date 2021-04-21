"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def func(a, b):
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    cache_value = dict()

    def the_wrapper(a, b):
        new_value = None
        if new_value in cache_value:
            return cache_value[new_value]
        cache_value[new_value] = func(a, b)
        calculation = cache_value[new_value]
        return calculation

    return the_wrapper


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

print(val_1)
print(val_2)
assert val_1 is val_2
print(val_1 is val_2)
