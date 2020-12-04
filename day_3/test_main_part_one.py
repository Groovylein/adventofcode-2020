import pytest
import os
from day_3 import main

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file = os.path.join(current_dir, 'test_input.txt')
test_input_file_simple = os.path.join(current_dir, 'test_input_simple.txt')

def test_input():
    expected_dict = {
        (0,0) : ".",
        (0,1) : ".",
        (1,0) : "#",
        (1,1) : ".",
        (2,0) : ".",
        (2,1) : "#",
        (3,0) : ".",
        (3,1) : ".",
    }
    input_dict = main.read_input(test_input_file_simple)
    assert input_dict == expected_dict