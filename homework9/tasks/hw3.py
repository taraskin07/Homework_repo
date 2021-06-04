"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
#>>> universal_file_counter(test_dir, "txt")
6
#>>> universal_file_counter(test_dir, "txt", str.split)
6

"""

from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    p = dir_path
    counter = 0
    files = Path(p).rglob(f"*.{file_extension}")
    for file in files:
        with open(file) as f:
            if tokenizer == None:
                counter += len(list(f))
            else:
                words = f.read()
                counter += len(tokenizer(words))
    return counter


if __name__ == "__main__":
    path_to_files = Path(__file__).parents[1].joinpath("tests")
    print(universal_file_counter(path_to_files, "txt", str.split))
    print(universal_file_counter(path_to_files, "txt"))
