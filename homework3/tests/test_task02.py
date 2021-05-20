from homework3.tasks.task02 import *


def test_timer_func():
    t = time.perf_counter()
    func_with_pool()
    sec = time.perf_counter() - t
    assert sec <= 60
    print(f"Estimated time is: {sec:.2f} seconds")
