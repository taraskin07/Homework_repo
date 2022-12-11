import os

import pytest
from homework08.tasks.task1 import KeyValueStorage

path = os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.join(path, "test_task1.txt")


def test_text_contents():
    path = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(path, "test_task1.txt")
    storage = KeyValueStorage(abs_path)
    assert storage["name"] == "kek"
    assert storage.song_name == "shadilay"
    assert storage.power == 9001
    assert storage.last_name == "top"
    assert storage["dictionary"] == "test"


def test_error_raised(tmpdir):
    p = tmpdir.join("something.txt")
    p.write("1=something")
    with pytest.raises(ValueError):
        storage = KeyValueStorage(p)
        assert storage["1"]
        assert storage[1]
