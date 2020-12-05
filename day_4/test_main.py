import os

from day_4 import main

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file = os.path.join(current_dir, 'test_input.txt')
test_input_file_simple = os.path.join(current_dir, 'test_input_simple.txt')


def test_transform_data():
    expected_list = [
        {"ecl": "gry",
         "pid": "860033327",
         "eyr": "2020",
         "hcl": "#fffffd"},
        {"hcl": "#cfa07d",
         "byr": "1929"}
    ]

    returned_list = main.transform_data(test_input_file_simple)
    assert returned_list == expected_list


def test_check_data():
    returned_list = main.transform_data(test_input_file)
    valid_passports = main.check_data(returned_list)
    assert valid_passports == 2
