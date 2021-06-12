"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

#>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


@contextmanager
def suppressor(p_exception):
    try:
        yield
    except p_exception:
        pass


class Suppressor_cl:
    def __init__(self, p_exception):
        self.p_exception = p_exception
        print(p_exception)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type == self.p_exception
