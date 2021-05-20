from homework3.tasks.task03 import *


def test_positive_even():
    functions = (lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
    positive_even = Filter(functions)
    positive_case = positive_even.apply(range(100))
    assert positive_case == [value for value in positive_case if value % 2 == 0]


def test_sample_data():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    filter_return = make_filter(name="polly", type="bird").apply(sample_data)
    assert filter_return == [sample_data[1]]
