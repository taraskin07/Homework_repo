from homework7.tasks.hw2 import backspace_compare


def test_input_check_pos():
    s = "ab#c"
    t = "ad#c"
    assert backspace_compare(s, t)

    s = "a##c"
    t = "#a#c"
    assert backspace_compare(s, t)

    s = "##c"
    t = "cccc###"
    assert backspace_compare(s, t)

    s = "##"
    t = "###"
    assert backspace_compare(s, t)

    s = "##"
    t = ""
    assert backspace_compare(s, t)


def test_input_check_neg():
    s = "a#c"
    t = "b"
    assert not backspace_compare(s, t)

    s = "a#c"
    t = "ac"
    assert not backspace_compare(s, t)
