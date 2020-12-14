import os

from day_10 import main

current_dir = os.path.dirname(os.path.abspath(__file__))
test_input_file_1 = os.path.join(current_dir, 'test_input_1.txt')
with open(test_input_file_1, "r") as openfile:
    numbers_in_file_1 = [int(n) for n in openfile.read().splitlines()]
test_input_file_2 = os.path.join(current_dir, 'test_input_2.txt')
with open(test_input_file_2, "r") as openfile:
    numbers_in_file_2 = [int(n) for n in openfile.read().splitlines()]


def test_get_jolts_1():
    one_jolt, three_jolts = main.get_adapter_jolts(numbers_in_file_1)
    assert one_jolt == 7
    assert three_jolts == 5


def test_arrangements_1():
    arrangement = main.create_arrangements(numbers_in_file_1)

    assert len(arrangement) == 8


def test_get_jolts_2():

    one_jolt, three_jolts = main.get_adapter_jolts(numbers_in_file_2)
    assert one_jolt == 22
    assert three_jolts == 10
