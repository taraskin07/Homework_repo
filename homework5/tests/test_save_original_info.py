import functools

from homework5.tasks.save_original_info import custom_sum, print_result


def custom_sum(*args):
    """This function can sum any objects which have __add__"""

    return functools.reduce(lambda x, y: x + y, args)


def test_custom_sum():
    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert custom_sum(1, 2, 3, 4) == 10


def test_doc_and_name():

    global custom_sum
    custom_sum([1, 2, 3], [4, 5])
    doc1 = custom_sum.__doc__
    name1 = custom_sum.__name__

    custom_sum = print_result(custom_sum)
    custom_sum([1, 2, 3], [4, 5])
    doc2 = custom_sum.__doc__
    name2 = custom_sum.__name__

    assert doc1 == doc2
    assert name1 == name2
