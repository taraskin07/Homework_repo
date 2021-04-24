from homework1.sample_project.calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_is_integer():
    """Testing that variable is integer"""
    assert not isinstance("input_variable", int)


def test_is_bool():
    """Testing that function return boolean value"""
    assert isinstance(check_power_of_2(2), bool)
