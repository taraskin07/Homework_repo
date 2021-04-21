"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
import string


def custom_range(string, *args):
    unique_values = list(string)
    range_values = list(args)
    new_list = []
    start = 0
    stop = len(unique_values)
    step = 1
    for id, value in enumerate(range_values):
        if value in unique_values:
            if len(range_values) == 1:
                stop = unique_values.index(range_values[0])
            elif id == 0:
                start = unique_values.index(range_values[0])
            elif id == 1:
                stop = unique_values.index(range_values[1])
        else:
            if id == 2:
                step = range_values[2]
    for number in range(start, stop, step):
        new_list.append(unique_values[number])
    return new_list


print(custom_range(string.ascii_lowercase, "g"))
print(custom_range(string.ascii_lowercase, "g", "p"))
print(custom_range(string.ascii_lowercase, "p", "g", -2))

assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]
assert custom_range(string.ascii_lowercase, "g", "p") == [
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
]
assert custom_range(string.ascii_lowercase, "p", "g", -2) == ["p", "n", "l", "j", "h"]
