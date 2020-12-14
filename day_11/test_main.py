import os

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file = os.path.join(current_dir, 'test_input.txt')


def test_first_iteration():
    assert True