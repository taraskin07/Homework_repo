import hashlib
import random
import struct
import time
from multiprocessing import Pool, Process, Queue

res = Queue


def wrapper(*args):
    print("here")
    value = slow_calculate(*args)
    res.put(value)


def func(interval):
    p = [threading.Thread(target=wrapper, args=(i,), daemon=True) for i in interval]
    [th.start() for th in p]
    [th.join() for th in p]


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    print(f"i start {value}", res)
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


if __name__ == "__main__":
    interval = [range(20 * i, (i + 1) * 20) for i in range(25)]
    with Pool(20) as p:
        p.map(func, interval)

    print(res)


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
