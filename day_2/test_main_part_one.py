import os
from day_2 import main

test_input_condition_list = []
test_input_password_list = []
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, 'test_input.txt')
with open(input_file, "r") as openfile:
    for line in openfile:
        line = line.strip()
        test_input_condition, test_input_password = line.split(":")
        test_input_condition_list.append(test_input_condition)
        test_input_password_list.append(test_input_password)


def test_valid_1():
    test_input_condition_1 = test_input_condition_list[0]
    test_input_password_1 = test_input_password_list[0]

    valid_password = main.password_validation_part_one(test_input_condition_1, test_input_password_1)
    assert valid_password is True

def test_invalid():
    test_input_condition_2 = test_input_condition_list[1]
    test_input_password_2 = test_input_password_list[1]

    valid_password = main.password_validation_part_one(test_input_condition_2, test_input_password_2)
    assert valid_password is False

def test_valid_2():
    test_input_condition_3 = test_input_condition_list[2]
    test_input_password_3 = test_input_password_list[2]

    valid_password = main.password_validation_part_one(test_input_condition_3, test_input_password_3)
    assert valid_password is True

