import hashlib
import random
import struct
import time
from multiprocessing import Pool
from threading import Thread


class ThreadWithReturnValue(Thread):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None
    ):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        # print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def func(interval):
    p = [ThreadWithReturnValue(target=slow_calculate, args=(i,)) for i in interval]
    [th.start() for th in p]
    result = [th.join() for th in p]
    print(result)
    return sum(result)


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    # print(f"i start {value}", res)
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def func_with_pool():
    interval = [range(20 * i, (i + 1) * 20) for i in range(25)]
    with Pool(4) as p:
        summa = sum(p.map(func, interval))
        print(summa)
    return summa


if __name__ == "__main__":
    func_with_pool()
