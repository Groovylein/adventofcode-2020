import os
import pytest

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

@pytest.mark.parametrize("hcl, return_value",
                         [("#123abc", True),
                          ("#123abz", False),
                          ("123abc", False),
                          ])
def test_check_hair(hcl, return_value):
    assert main.check_hair(hcl) is return_value


@pytest.mark.parametrize("hgt, return_value",
                         [("60in", True),
                          ("190cm", True),
                          ("175cm", True),
                          ("190in", False),
                          ("190", False)])
def test_check_height(hgt, return_value):
    assert main.check_height(hgt) is return_value


@pytest.mark.parametrize("pid, return_value",
                         [("000000001", True),
                          ("123456789", True),
                          ("0123456789", False)])
def test_check_pid(pid, return_value):
    assert main.check_pid(pid) is return_value
