"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


my_precious_logger("error: file not found")
# stderr
'error: file not found'


my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""
import sys

from homework04.tasks.task_3_get_print_output import my_precious_logger


def test_my_precious_logger_error(capsys):
    my_precious_logger("error: file not found")

    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


def test_my_precious_logger_output(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK"
