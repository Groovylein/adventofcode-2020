import os

from day_10 import main

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file_1 = os.path.join(current_dir, 'test_input_1.txt')
test_input_file_2 = os.path.join(current_dir, 'test_input_2.txt')


def test_get_jolts_1():

    with open(test_input_file_1, "r") as openfile:
        numbers_in_file = [int(n) for n in openfile.read().splitlines()]
    one_jolt, three_jolts = main.get_adapter_jolts(numbers_in_file)
    assert one_jolt == 7
    assert three_jolts == 5


def test_get_jolts_2():

    with open(test_input_file_2, "r") as openfile:
        numbers_in_file = [int(n) for n in openfile.read().splitlines()]
    one_jolt, three_jolts = main.get_adapter_jolts(numbers_in_file)
    assert one_jolt == 22
    assert three_jolts == 10