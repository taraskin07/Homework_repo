"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import codecs
import os
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    words_as_they_are = file_path.read().split()
    words = []
    for id, whole_word in enumerate(words_as_they_are):
        if whole_word.endswith("-", -1):
            whole_word = whole_word.replace("-", "")
            words_as_they_are[id] = whole_word + words_as_they_are[id + 1]
            words.append(words_as_they_are[id])
            words_as_they_are.remove(words_as_they_are[id + 1])
        else:
            words.append(whole_word)

    unique_chars_length = 0
    longest_10_words = []
    for unique_chars in words:
        if len(set(unique_chars)) >= unique_chars_length:
            unique_chars_length = len(set(unique_chars))
            longest_10_words.append(unique_chars)
    return longest_10_words[-10:]


def get_rarest_char(file_path: str) -> str:
    words_as_they_are = file_path.read().split()
    letters = "".join(sorted(words_as_they_are))
    count = None
    rare = None
    another_rare = None
    min = len(letters)
    sorted_set = sorted(list(set(letters)))
    for letter in sorted_set:
        count = letters.count(letter)
        if count < min:
            min = count
            rare = letter
        elif count == min:
            another_rare = letter

    return (min, rare, another_rare)


def count_punctuation_chars(file_path: str) -> int:
    words_as_they_are = file_path.read().split()
    letters = "".join(sorted(words_as_they_are))
    count1 = letters.count(",")
    count2 = letters.count(".")
    count3 = letters.count(":")
    count4 = letters.count(")")
    count5 = letters.count("(")
    count6 = letters.count("!")
    count7 = letters.count("?")
    count = count1 + count2 + count3 + count4 + count5 + count6 + count7
    return count


def count_non_ascii_chars(file_path: str) -> int:
    words_as_they_are = file_path.read().split()
    letters = "".join(sorted(words_as_they_are))
    count = 0
    sorted_set = sorted(list(set(letters)))
    for letter in sorted_set:
        if not letter.isascii():
            count += letters.count(letter)
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    words_as_they_are = file_path.read().split()
    letters = "".join(sorted(words_as_they_are))
    max = 0
    frequent = None
    sorted_set = sorted(list(set(letters)))
    for letter in sorted_set:
        if not letter.isascii():
            max = letters.count(letter)
            frequent = letter
    return max, frequent


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(path, "data.txt")
    with codecs.open(abs_path, "r", encoding="unicode-escape") as fi:
        print(get_longest_diverse_words(fi))
    with codecs.open(abs_path, "r", encoding="unicode-escape") as fi:
        print(get_rarest_char(fi))
    with codecs.open(abs_path, "r", encoding="unicode-escape") as fi:
        print(count_punctuation_chars(fi))
    with codecs.open(abs_path, "r", encoding="unicode-escape") as fi:
        print(get_most_common_non_ascii_char(fi))
