from homework02.tasks.hw2 import major_and_minor_elem


def test_example_check_major_and_minor_elem():
    ex1 = [3, 2, 3]
    ex2 = [2, 2, 1, 1, 1, 2, 2]
    assert major_and_minor_elem(ex1) == (3, 2)
    assert major_and_minor_elem(ex2) == (2, 1)


if __name__ == "__main__":
    print(major_and_minor_elem(ex1))
    print(major_and_minor_elem(ex2))
