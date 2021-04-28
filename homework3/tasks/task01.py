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


def func(a, b):  # Сама функция, которую надо задекорировать
    return (a ** b) ** 2


def new_cache(
    times,
):  # Параметризованный декоратор, где параметр times говорит сколько раз нужно закэшировать значение, если times=3, значит 3 раза, не учитывая самый первый вызов, когда значение кэшировалось
    counter = 0
    cache_value = dict()

    def cache_func(
        func: Callable,
    ) -> Callable:  # функция принимающая на вход искомую функцию func, объявленную раньше
        def the_wrapper(
            a, b
        ):  # функция принимающая на вход значения аргументов функции func, объявленной ранее
            nonlocal counter, cache_value
            new_value = (
                a,
                b,
            )  # кортеж с аргументами искомой функции func, объявленной ранее, так просто, для удобства восприятия
            if (
                counter >= times
            ):  # проверяем, не обратились ли мы к кэшу более 3х раз, по умолчанию counter == 1
                cache_value.clear()  # если же это уже 4-е обращение, очищаем кэш
                counter = 0  # если же это уже 4-е обращение, сбрасываем счетчик обращений на исходную counter == 1
            if (
                new_value in cache_value
            ):  # а вот если это уже 2-е или 3-е обращение (up to 'times' value)
                counter += 1  # увеличиваем счетчик на 1
                return cache_value[new_value]  # возвращаем результат из словаря
            cache_value[new_value] = func(
                a, b
            )  # в противном случае, записываем результат в словарь
            calculation = cache_value[
                new_value
            ]  # для красоты обзываем этот результат новой переменной, которую затем и возвращаем
            return calculation  # возвращаем тут

        return the_wrapper

    return cache_func


@new_cache(times=3)  # декорируем эту несчастную функцию
def func(a, b):
    return (a ** b) ** 2


if __name__ == "__main__":
    some = 100, 200

    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)
    val_4 = func(*some)
    val_5 = func(*some)
    print(val_1)
    print(val_2)
    print(val_3)
    print(val_4)
    print(val_5)
    print(val_1 is val_2)  # кэшируются ли 1й и 2й вызов функции, True
    print(val_2 is val_3)  # кэшируются ли 2й и 3й вызов функции, True
    print(val_3 is val_4)  # кэшируются ли 3й и 4й вызов функции, True
    print(
        val_4 is val_5
    )  # кэшируются ли 4й и 5й вызов функции, False, 5й уже не из кэша, считается заново
