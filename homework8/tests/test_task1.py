import os

import pytest
from homework8.tasks.task1 import KeyValueStorage

path = os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.join(path, "test_task1.txt")


def test_text_contents():
    storage = KeyValueStorage(abs_path)
    assert storage["name"] == "kek"
    assert storage.song_name == "shadilay"
    assert storage.power == 9001
    assert storage.last_name == "top"


def test_error_raised():
    storage = KeyValueStorage(abs_path)
    with pytest.raises(KeyError):
        assert storage[1]
