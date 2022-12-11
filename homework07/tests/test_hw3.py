from homework07.tasks.hw3 import tic_tac_toe_checker


def test_unfinished():
    unfinished = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(unfinished) == "unfinished"


def test_x_wins():
    x_wins1 = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(x_wins1) == "x wins!"

    x_wins2 = [["-", "-", "x"], ["-", "o", "x"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(x_wins2) == "x wins!"

    x_wins3 = [["-", "-", "x"], ["-", "x", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(x_wins3) == "x wins!"


def test_o_wins():
    o_wins1 = [["o", "x", "o"], ["x", "o", "o"], ["o", "o", "x"]]
    assert tic_tac_toe_checker(o_wins1) == "o wins!"

    o_wins2 = [["o", "x", "o"], ["x", "o", "o"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(o_wins2) == "o wins!"

    o_wins3 = [["o", "x", "x"], ["o", "o", "o"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(o_wins3) == "o wins!"


def test_draw_case():
    draw = [["o", "x", "o"], ["x", "o", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(draw) == "draw!"


def test_that_hyphen_is_an_empty_character():
    """
    You cannot win using '-' character!
    """

    hyphen1 = [["o", "x", "-"], ["x", "-", "o"], ["-", "o", "x"]]
    assert tic_tac_toe_checker(hyphen1) == "unfinished"

    hyphen2 = [["o", "x", "-"], ["-", "-", "-"], ["o", "o", "x"]]
    assert tic_tac_toe_checker(hyphen2) == "unfinished"

    hyphen3 = [["o", "x", "-"], ["x", "-", "-"], ["o", "o", "-"]]

    assert tic_tac_toe_checker(hyphen3) == "unfinished"
