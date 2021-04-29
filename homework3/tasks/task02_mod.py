import hashlib
import random
import struct
import time
from multiprocessing import Array, Pool, Process, Queue


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


# @how_long_decorator
def calculation_of_several_processes(func):
    with Pool(4) as p:
        summa = sum(p.map(func, range))
    return f"The sum is: {summa}"


def summator(numbers, result):
    for id, value in enumerate(numbers):
        result[id] = slow_calculate(value)


if __name__ == "__main__":
    numbers = range(100)
    result = Array("i", 100)
    p = Process(target=summator, args=(numbers, result))
    p.start()
    p.join()
    sum1 = sum(result[:])

    # a = Array('i', range(101))
    # b = Array('i', range(100,201))
    # c = Array('i', range(200,301))
    # d = Array('i', range(300, 401))
    # e = Array('i', range(400, 501))
    # p = Process(target=calculation_of_several_processes(slow_calculate), args=(a, b, c, d, e))
    # p.start()
    # p.join()


# res = Queue
#
#
# def wrapper(*args):
#     print("here")
#     value = slow_calculate(*args)
#     res.put(value)
#
#
# def func(interval):
#     p = [threading.Thread(target=wrapper, args=(i,), daemon=True) for i in interval]
#     [th.start() for th in p]
#     [th.join() for th in p]
#
#
# def slow_calculate(value):
#     """Some weird voodoo magic calculations"""
#     print(f"i start {value}", res)
#     time.sleep(random.randint(1, 3))
#     data = hashlib.md5(str(value).encode()).digest()
#     return sum(struct.unpack("<" + "B" * len(data), data))
#
#
# if __name__ == "__main__":
#     interval = [range(20 * i, (i + 1) * 20) for i in range(25)]
#     with Pool(20) as p:
#         p.map(func, interval)
#
#     print(res)


# def to_form_a_queue(q):
#     t = Process(target=slow_calculate, args=(values,))
#     t.start()
#     q.put(values)
#     t.join()
#
# def to_get_from_queue():
#     q = Queue()
#     p = Process(target=to_form_a_queue, args=(q,))
#     p.start()
#     summa = sum(q.get())
#     p.join()
#     return summa
#
#
#
# def to_sum_calculations(list_of_numbers):
#     t = time.perf_counter()
#     sum = 0
#     with Pool(processes=5) as pool:
#         results = [pool.apply_async(slow_calculate, ()) for i in range(4)]
#         seconds = (time.perf_counter() - t)
#         return sum, seconds
#
# if __name__ == "__main__":
#     list_of_numbers = [(0, 101), (100, 201), (200, 301), (300, 401), (400, 501)]
#     print(to_sum_calculations(list_of_numbers))


# if __name__ == "__main__":
#     t = time.perf_counter()
#     q = Queue()
#     with Pool(processes=4) as pool:
#         for i in pool.imap_unordered(slow_calculate, range(501)):
#             q.put(i)
#         summa = 0
#         summa += q.get()
#         seconds = time.perf_counter() - t
#         print(summa, seconds)
