import os

from day_9 import main

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file = os.path.join(current_dir, 'test_input.txt')


def test_invalid_xmas():
    test_preable_list, test_number_list = main.convert_input(test_input_file, 5)
    invalid_number = main.search_invalid_xmas(test_preable_list, test_number_list)
    assert invalid_number == 127
