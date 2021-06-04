from pathlib import Path

from homework9.tasks.hw3 import universal_file_counter

path_to_files = Path(__file__).parents[1].joinpath("tests")


def test_counter_without_tokenizer():
    assert universal_file_counter(path_to_files, "txt") == 6


def test_counter_with_tokenizer():
    assert universal_file_counter(path_to_files, "txt", str.split) == 6


def test_mocking_files(tmpdir):
    f1 = tmpdir.join("fileone.txt")
    f2 = tmpdir.join("filetwo.txt")
    f3 = tmpdir.join("filethree.txt")
    f4 = tmpdir.join("filefour.txt")
    f1.write("1\n3\n5\n2\n4\n6\n")
    f2.write("2\n4\n6\n8\n10\n12\n")
    f3.write("7\n9\n11\n8\n10\n12\n")
    f4.write("1\n2\n3\n4\n5\n6\n")
    path_to_files = Path(f1).parent

    assert universal_file_counter(path_to_files, "txt") == 24
    assert universal_file_counter(path_to_files, "txt", str.split) == 24
