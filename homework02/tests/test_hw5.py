import string

from homework02.tasks.hw5 import custom_range


def test_conditions_and_examples():
    """All given examples are checked"""
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
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
