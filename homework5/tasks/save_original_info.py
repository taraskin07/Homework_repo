"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func

print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий

До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция

Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add__'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def save_original_info(function):
    """New wrapper which gives name and docstring of the original function"""

    def new_wrapper(new_func):
        new_func.__name__ = function.__name__
        new_func.__doc__ = function.__doc__
        new_func.__original_func = function
        return new_func

    return new_wrapper


def print_result(func):
    @save_original_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of the original function"""

        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add__"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func
    print("-" * 10)
    logger.debug("# the result returns without printing")
    without_print(1, 2, 3, 4)
    print(custom_sum.__original_func)
