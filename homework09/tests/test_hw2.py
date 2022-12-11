import pytest
from homework09.tasks.hw2 import Suppressor_cl, suppressor


def test_Suppressor_cl():
    with Suppressor_cl(IndexError):
        [][2]


def test_suppressor():
    with suppressor(IndexError):
        [][2]


def test_index_error():
    with pytest.raises(IndexError):
        [][2]


def test_type_error_Suppressor_cl():
    with Suppressor_cl(TypeError):
        2 + "str"


def test_type_error_suppressor():
    with suppressor(TypeError):
        2 + "str"


def test_that_type_error():
    with pytest.raises(TypeError):
        2 + "str"


def test_type_error_Suppressor_cl():
    with Suppressor_cl(NameError):
        2 + not_defined


def test_type_error_suppressor():
    with suppressor(NameError):
        2 + not_defined


def test_that_type_error():
    with pytest.raises(NameError):
        2 + not_defined
