from tasks.hw2 import major_and_minor_elem

ex1 = [3, 2, 3]
print(major_and_minor_elem(ex1))
ex2 = [2, 2, 1, 1, 1, 2, 2]
print(major_and_minor_elem(ex2))


def example_check_major_and_minor_elem():
    assert major_and_minor_elem(ex1) == (3, 2)
    assert major_and_minor_elem(ex2) == (2, 1)
