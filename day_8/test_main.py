import os

from day_8 import main

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file = os.path.join(current_dir, 'test_input.txt')


def test_get_loop():
    returned_acc = main.get_loop(test_input_file)
    assert returned_acc == 5


def test_fix_loop():
    returned_acc = main.fix_loop(test_input_file)
    assert returned_acc == 8
