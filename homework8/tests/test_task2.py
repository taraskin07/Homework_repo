from homework8.tasks.task2 import TableData

books = TableData(database_name="example.sqlite", table_name="books")
presidents = TableData(database_name="example.sqlite", table_name="presidents")


def test_length_assertion():
    assert len(presidents) == 3
    assert len(books) == 3


def test_contains():
    assert "Yeltsin" in presidents
    assert "Trump" in presidents
    assert "Big Man Tyrone" in presidents
    assert not "Obama" in presidents
    assert "1984" in books


def test_iteration():
    new_list = []
    for president in presidents:
        new_list.append(president["name"])
    assert new_list == ["Yeltsin", "Trump", "Big Man Tyrone"]
    new_list2 = []
    for book in books:
        new_list2.append(book["name"])
    assert new_list2 == ["Farenheit 451", "Brave New World", "1984"]


def test_content():
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert books["Farenheit 451"] == ("Farenheit 451", "Bradbury")
