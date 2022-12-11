import os

from homework10.tasks.hw1 import gen_sorting, merge_sorted_files


def test_nested_lists():
    nl1, nl2 = [
        [1, 3, 76],
        [
            1,
            53,
            467,
        ],
    ]
    assert list(gen_sorting(iter(nl1), iter(nl2))) == [1, 1, 3, 53, 76, 467]
    nl3, nl4 = [[1, 3, 5], [2, 4, 6]]
    assert list(gen_sorting(iter(nl3), iter(nl4))) == [1, 2, 3, 4, 5, 6]


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
