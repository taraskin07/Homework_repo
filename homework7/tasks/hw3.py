"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return f"{board[1][1]} wins!"
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        return f"{board[1][1]} wins!"
    for string, massive in enumerate(board):
        if massive[0] == massive[1] == massive[2] != "-":
            return f"{massive[1]} wins!"
        elif board[0][string] == board[1][string] == board[2][string] != "-":
            return f"{board[0][string]} wins!"
    for massive in board:
        if "-" in massive:
            return f"unfinished"
        else:
            return f"draw!"


if __name__ == "__main__":
    ex1 = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
    ex2 = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    ex3 = [["o", "x", "o"], ["x", "o", "o"], ["o", "o", "x"]]
    ex4 = [["o", "x", "o"], ["x", "o", "o"], ["x", "o", "x"]]
    ex5 = [["o", "x", "-"], ["x", "-", "o"], ["-", "o", "x"]]

    print(tic_tac_toe_checker(ex1))
    print(tic_tac_toe_checker(ex2))
    print(tic_tac_toe_checker(ex3))
    print(tic_tac_toe_checker(ex4))
    print(tic_tac_toe_checker(ex5))
