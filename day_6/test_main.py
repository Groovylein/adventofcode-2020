import os

from day_6 import main

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file = os.path.join(current_dir, 'test_input.txt')


def test_transform_input():
    expected_list = [["a", "b", "c"], ["a", "b", "c"], ["a", "b", "c"], ["a"], ["b"]]
    returned_dict = main.transform_input(test_input_file)

    assert returned_dict == expected_list
    assert len(returned_dict[0]) == 3
    assert len(returned_dict[1]) == 3
    assert len(returned_dict[2]) == 3
    assert len(returned_dict[3]) == 1
    assert len(returned_dict[4]) == 1
