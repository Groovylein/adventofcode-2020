import pytest
import os
from day_3 import main

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file = os.path.join(current_dir, 'test_input.txt')
test_input_file_simple = os.path.join(current_dir, 'test_input_simple.txt')


def test_input():
    expected_list = [
        [".", "."],
        ["#", "."],
        [".", "#"],
        [".", "."],
    ]
    input_list = main.read_input(test_input_file_simple)
    assert input_list == expected_list


def test_run():

    input_list = main.read_input(test_input_file)

    trees = main.toboggan_run(input_list, 3, 1)

    assert trees == 7