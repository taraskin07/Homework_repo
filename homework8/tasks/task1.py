import os
from keyword import iskeyword


class KeyValueStorage:
    """
    A wrapper class for key=value storage (as a file).
    Each line in file is represented as key and value separated by '=' symbol.
    Values can be strings or integer numbers.
    If a value can be treated both as a number and a string, it is treated as number.
    """

    def __init__(self, path_to_file):
        """
        :param path_to_file: Takes path to the file.
        """
        self.dictionary = dict()
        with open(path_to_file, "r") as fi:
            builtins = frozenset(KeyValueStorage.__dict__.keys())
            for line in fi:
                key, value = line.strip("\n").split("=")
                if key not in builtins:
                    if iskeyword(key):
                        raise ValueError("It is not a proper keyword")
                    try:
                        if isinstance(int(value), int):
                            value = int(value)
                            self.dictionary[key] = value
                    except ValueError:
                        self.dictionary[key] = value

    def __getitem__(self, key):
        """
        :return: Value defined for the 'key'
        """
        return self.dictionary[key]

    def __getattr__(self, key):
        """
        :return: Value defined for the 'key'
        """
        return self.dictionary[key]


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(path, "task1.txt")
    storage = KeyValueStorage(abs_path)
    print(storage["name"])
    print(storage.song_name)
    print(storage.power)
