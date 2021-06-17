"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""

from pathlib import Path
from typing import Iterator, List, Union


def gen_sorting(it1, it2):
    el1 = next(it1, None)
    el2 = next(it2, None)
    while el1 or el2:
        if not el1 or (el2 and el2 < el1):
            yield el2
            el2 = next(it2, None)
        else:
            yield el1
            el1 = next(it1, None)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    new_list = []
    for f_name in file_list:
        with open(f_name) as f:
            lines = [int(line.rstrip("\n")) for line in f]
            new_list.append(lines)
    list1, list2 = new_list

    return gen_sorting(iter(list1), iter(list2))


if __name__ == "__main__":
    path_to_file1 = Path(__file__).parents[1].joinpath("tests").joinpath("file1.txt")
    path_to_file2 = Path(__file__).parents[1].joinpath("tests").joinpath("file2.txt")
    print(list(merge_sorted_files([path_to_file1, path_to_file2])))
    nl1, nl2 = [
        [1, 3, 76],
        [
            1,
            53,
            467,
        ],
    ]
    nl3, nl4 = [[1, 3, 5], [2, 4, 6]]
    print(list(gen_sorting(iter(nl1), iter(nl2))))
    print(list(gen_sorting(iter(nl3), iter(nl4))))
