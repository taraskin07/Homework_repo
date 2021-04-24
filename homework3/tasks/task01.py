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

cache_value = dict()
counter = 1


def new_cache(times):
    def cache_func(func: Callable) -> Callable:
        def the_wrapper(a, b):
            global cache_value, counter
            new_value = (a, b)
            if counter >= times:
                cache_value.clear()
                counter = 1
                return func(a, b)
            if new_value in cache_value:
                counter += 1
                return cache_value[new_value]
            cache_value[new_value] = func(a, b)
            calculation = cache_value[new_value]
            return calculation

        return the_wrapper

    return cache_func


@new_cache(times=3)
def func(a, b):
    return (a ** b) ** 2


if __name__ == "__main__":
    some = 100, 200

    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)
    val_4 = func(*some)

    print(val_1)
    print(val_2)
    print(val_3)
    print(val_4)
    print(val_3 is val_4)
