import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        """
        :param database_name: name of the database
        :param table_name: name of table in database
        """
        self.database_name = database_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.cursor().close()
        self.conn.close()

    def __len__(self):
        """
        Count how many rows in the table.
        :return: integer, natural number
        :rtype: int
        """
        self.cursor.execute(f"SELECT count(*) FROM {self.table_name}")
        return self.cursor.fetchone()[0]

    def __getitem__(self, value):
        """
        This method get all records with this name.
        :param value: Table value
        :return: Should return single data row for table with name == 't_name'
        """

        self.cursor.execute(
            f"SELECT * FROM {self.table_name} WHERE name=:name", {"name": value}
        )
        return self.cursor.fetchone()

    def __contains__(self, value):
        """
        Checking whether value is in table.
        :param value:
        :return: boolean
        :rtype: bool
        """
        self.cursor.execute(
            f'SELECT name FROM {self.table_name} where name = "{value}"'
        )
        data = self.cursor.fetchall()
        return bool(data)

    def __iter__(self):
        """
        Making table rows iterable.
        :return: a new iterator object that can iterate over all the objects in the collection
        """

        def dictionary_gen(row):
            dictionary = {}
            for id, val in enumerate(self.cursor.description):
                dictionary[val[0]] = row[id]
            return dictionary

        yield from (
            dictionary_gen(row)
            for row in self.cursor.execute(f"SELECT * FROM {self.table_name}")
        )


if __name__ == "__main__":
    with TableData(
        database_name="example.sqlite", table_name="presidents"
    ) as presidents:
        for president in presidents:
            print(president["name"])
        print(presidents["Yeltsin"])
        print("Yeltsin" in presidents)
        print("Obama" in presidents)
        print(len(presidents))
    with TableData(database_name="example.sqlite", table_name="books") as books:
        for book in books:
            print(book["name"])
        print(books["Farenheit 451"])
        print("1984" in books)
        print(len(books))
