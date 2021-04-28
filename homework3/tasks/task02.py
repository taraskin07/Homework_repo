import hashlib
import random
import struct
import time
from multiprocessing import Pool, Process, Queue
from typing import List


def how_long_decorator(func):
    """Decorator that calculates time!"""
    import time

    def wrapper(*args):
        t = time.perf_counter()
        res = func(*args)
        print(
            f"Estimated time for the {func.__name__} is no longer than {(time.perf_counter() - t):.2f} seconds!"
        )
        return res

    return wrapper


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


if __name__ == "__main__":
    # values = [number for number in range(501)]

    @how_long_decorator
    def calculation_of_several_processes():
        with Pool(4) as p:
            summa = sum(p.map(slow_calculate, range(501)))
        return f"The sum is: {summa}"

    print(calculation_of_several_processes())
