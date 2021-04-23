import codecs

from homework2.tasks.hw1 import *


def test_get_longest_diverse_words():
    """Testing that 10 last words are the longest and in ordered fashion instead of random"""
    with codecs.open(
        "C:\\Users\\AngryKid\\Repositories\\Homework_repo\\homework2\\tests\\data.txt",
        "r",
        encoding="unicode-escape",
    ) as fi:
        new_list = get_longest_diverse_words(fi)
        count = -10
        while count != -2:
            assert len(new_list[count]) - len(new_list[count]) >= 0


def test_get_rarest_char():
    """Testing that rarest char should appear only 1 time"""
    with codecs.open(
        "C:\\Users\\AngryKid\\Repositories\\Homework_repo\\homework2\\tests\\data.txt",
        "r",
        encoding="unicode-escape",
    ) as fi:
        assert get_rarest_char(fi)[0] == 1


def test_count_punctuation_chars():
    """Testing that there are 4213 punctuation chars"""
    with codecs.open(
        "C:\\Users\\AngryKid\\Repositories\\Homework_repo\\homework2\\tests\\data.txt",
        "r",
        encoding="unicode-escape",
    ) as fi:
        assert count_punctuation_chars == 4213


def test_get_most_common_non_ascii_char():
    """Testing that the most common non ascii char is not ascii"""
    with codecs.open(
        "C:\\Users\\AngryKid\\Repositories\\Homework_repo\\homework2\\tests\\data.txt",
        "r",
        encoding="unicode-escape",
    ) as fi:
        assert not get_most_common_non_ascii_char(fi)[1].isascii()
