"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

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


def find_occurrences(tree: dict, element: Any) -> int:
    occurrences = 0
    if isinstance(tree, dict):
        tree = tree.values()
    for value in tree:
        if value == element:
            occurrences += 1
        if isinstance(value, (str, bool, int)):
            continue
        else:
            occurrences += find_occurrences(value, element)
    return occurrences


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))
    print(find_occurrences(example_tree, "BLUE"))
    print(find_occurrences(example_tree, "key1"))

    print(find_occurrences(example2, True))
    print(find_occurrences(example2, False))
    print(find_occurrences(example2, 4))
