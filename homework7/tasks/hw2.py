"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str):
    read_first = []
    for letter in first:
        if letter == "#":
            if read_first:
                read_first.pop()
        else:
            read_first.append(letter)

    first_str = "".join(read_first)

    read_second = []
    for letter in second:
        if letter == "#":
            if read_second:
                read_second.pop()
        else:
            read_second.append(letter)

    second_str = "".join(read_second)

    return first_str == second_str
