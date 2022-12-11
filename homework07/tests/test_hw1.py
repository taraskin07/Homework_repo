from homework7.tasks.hw1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

example2 = {
    "first": ["RED", False],
    "second": {
        "simple_key": ["simple", True, "of", "RED", False],
    },
    "third": {
        "abc": True,
        "jhl": False,
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", 4, "of", 4, {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def test_pos_find_occur():
    assert find_occurrences(example_tree, "RED") == 6
    assert find_occurrences(example_tree, "BLUE") == 2
    assert find_occurrences(example_tree, "value1") == 1


def test_neg_find_occur():
    assert find_occurrences(example_tree, "Black") == 0
    assert find_occurrences(example_tree, "key1") == 0


def test_my_example2():
    assert find_occurrences(example2, True) == 2
    assert find_occurrences(example2, False) == 3
    assert find_occurrences(example2, 4) == 2
