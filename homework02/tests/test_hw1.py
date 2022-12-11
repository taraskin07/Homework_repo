import codecs
import os

from homework02.tasks.hw1 import *


def test_get_longest_diverse_words():
    """Testing that 10 last words are the longest and in ordered fashion instead of random"""
    path = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(path, "data.txt")
    with codecs.open(
        abs_path,
        "r",
        encoding="unicode-escape",
    ) as fi:
        new_list = get_longest_diverse_words(fi)
        for count in range(-10, -2):
            assert len(set(new_list[count + 1])) - len(set(new_list[count])) >= 0


def test_get_rarest_char():
    """Testing that rarest char should appear only 1 time"""
    path = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(path, "data.txt")
    with codecs.open(
        abs_path,
        "r",
        encoding="unicode-escape",
    ) as fi:
        assert get_rarest_char(fi)[0] == 1


def test_count_punctuation_chars():
    """Testing that there are 4213 punctuation chars"""
    path = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(path, "data.txt")
    with codecs.open(
        abs_path,
        "r",
        encoding="unicode-escape",
    ) as fi:
        assert count_punctuation_chars(fi) == 4213


def test_get_most_common_non_ascii_char():
    """Testing that the most common non ascii char is not ascii"""
    path = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(path, "data.txt")
    with codecs.open(
        abs_path,
        "r",
        encoding="unicode-escape",
    ) as fi:
        assert not get_most_common_non_ascii_char(fi)[1].isascii()
