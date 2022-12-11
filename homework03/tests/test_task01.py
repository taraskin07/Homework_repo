from unittest.mock import Mock

from homework03.tasks.task01 import *


@new_cache(times=3)
def func(a, b):
    return (a**b) ** 2


def test_count_calls():
    """Testing that only 3 values are cached within 4 calls, 5th call - new calculation"""
    some = 100, 200
    mock_func = Mock()
    mock_decor = Mock()
    mock_decor.side_effect = new_cache(times=3)(mock_func)

    mock_decor(*some)
    calls_of_cache = mock_decor.call_count
    calls_of_func = mock_func.call_count
    assert calls_of_cache == 1
    assert calls_of_func == 1
    print(f"\n\nDecorator has been called {calls_of_cache} times")
    print(f"Function (to calculate value) has been called {calls_of_func} times")

    mock_decor(*some)
    calls_of_cache = mock_decor.call_count
    calls_of_func = mock_func.call_count
    print(f"\nDecorator has been called {calls_of_cache} times")
    print(f"Function (to calculate value) has been called {calls_of_func} times")
    assert calls_of_cache == 2
    assert calls_of_func == 1

    mock_decor(*some)
    calls_of_cache = mock_decor.call_count
    calls_of_func = mock_func.call_count
    print(f"\nDecorator has been called {calls_of_cache} times")
    print(f"Function (to calculate value) has been called {calls_of_func} times")
    assert calls_of_cache == 3
    assert calls_of_func == 1

    mock_decor(*some)
    calls_of_cache = mock_decor.call_count
    calls_of_func = mock_func.call_count
    print(f"\nDecorator has been called {calls_of_cache} times")
    print(f"Function (to calculate value) has been called {calls_of_func} times")
    assert calls_of_cache == 4
    assert calls_of_func == 1

    mock_decor(*some)
    calls_of_cache = mock_decor.call_count
    calls_of_func = mock_func.call_count
    print(f"\nDecorator has been called {calls_of_cache} times")
    print(f"Function (to calculate value) has been called {calls_of_func} times")
    assert calls_of_cache == 5
    assert calls_of_func == 2
