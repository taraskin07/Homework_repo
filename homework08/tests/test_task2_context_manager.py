import os

from homework08.tasks.task2_context_manager import TableData

path = os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.join(path, "example.sqlite")


def test_length_assertion_and_contain_presidents():
    with TableData(database_name=abs_path, table_name="presidents") as presidents:
        assert len(presidents) == 3
        assert "Yeltsin" in presidents
        assert "Trump" in presidents
        assert "Big Man Tyrone" in presidents
        assert not "Obama" in presidents


def test_iteration_presidents():
    with TableData(database_name=abs_path, table_name="presidents") as presidents:
        new_list = []
        for president in presidents:
            new_list.append(president["name"])
        assert new_list == ["Yeltsin", "Trump", "Big Man Tyrone"]


def test_content_presidents():
    with TableData(database_name=abs_path, table_name="presidents") as presidents:
        assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_length_assertion_and_contains_books():
    with TableData(database_name=abs_path, table_name="books") as books:
        assert len(books) == 3
        assert "1984" in books


def test_iteration_books():
    with TableData(database_name=abs_path, table_name="books") as books:
        new_list2 = []
        for book in books:
            new_list2.append(book["name"])
        assert new_list2 == ["Farenheit 451", "Brave New World", "1984"]


def test_content_books():
    with TableData(database_name=abs_path, table_name="books") as books:
        assert books["Farenheit 451"] == ("Farenheit 451", "Bradbury")
