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


def sorted_lists(lst):
    result = []
    for value in lst:
        for element in value:
            result.append(int(element))
            result = sorted(result)
    return result


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    list = []
    for f_name in file_list:
        with open(f_name) as f:
            lines = [int(line.rstrip("\n")) for line in f]
            list.append(lines)
    return iter(sorted_lists(list))


if __name__ == "__main__":
    print(list(merge_sorted_files(["file1.txt", "file2.txt"])))
    nl1 = [[1, 3, 76], [467], [3, 3, 3]]
    print(sorted_lists(nl1))
