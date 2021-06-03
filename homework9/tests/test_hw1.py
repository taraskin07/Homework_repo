import os

from homework9.tasks.hw1 import merge_sorted_files, sorted_lists


def test_nested_lists():
    nl1 = [[1, "2"], [], [5, 8, 0]]
    assert sorted_lists(nl1) == [0, 1, 2, 5, 8]
    nl2 = [[1, 3, 76], [467], [3, 3, 3]]
    assert sorted_lists(nl2) == [1, 3, 3, 3, 3, 76, 467]


def test_create_file(tmpdir):
    p = tmpdir.join("fileone.txt")
    p.write("2\n1\n0\n")
    assert p.read() == "2\n1\n0\n"
    assert len(tmpdir.listdir()) == 1
    assert os.path.exists(tmpdir.join("fileone.txt").strpath)


def test_merge_sorted_files(tmpdir):
    f1 = tmpdir.join("fileone.txt")
    f2 = tmpdir.join("filetwo.txt")
    f1.write("1\n3\n5\n")
    f2.write("2\n4\n6\n")
    assert list(merge_sorted_files([f1, f2])) == [1, 2, 3, 4, 5, 6]
