# I decided to write a code that generates data filtering object from a list of keyword parameters:


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(value):
            return keywords[key] == value

    filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


if __name__ == "__main__":
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    # example of usage:
    functions = (lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
    positive_even = Filter(functions)
    positive_case = positive_even.apply(range(100))
    print(positive_case)  # should return only even numbers from 0 to 99
    print([value for value in positive_case if value % 2 == 0])
    print(
        make_filter(name="polly", type="bird").apply(sample_data)
    )  # should return only second entry from the list
