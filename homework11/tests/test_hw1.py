from homework11.tasks.hw1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS", "BLACK")


def test_SimplifiedEnum():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.ORANGE == "ORANGE"
    assert ColorsEnum.BLACK == "BLACK"

    assert SizesEnum.XL == "XL"
    assert SizesEnum.L == "L"
    assert SizesEnum.M == "M"
    assert SizesEnum.XS == "XS"
