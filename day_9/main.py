import itertools
import os


def convert_input(input_file, pre):
    with open(input_file, "r") as openfile:
        input_as_list = [int(n) for n in openfile.read().splitlines()]
    preamble_list = input_as_list[:int(pre)]
    number_list = input_as_list[int(pre):]
    return preamble_list, number_list


def search_invalid_xmas(preamble_list, number_list):
    while True:
        search_num = number_list[0]
        sum_of_pre_list = [sum(n) for n in itertools.combinations(preamble_list, 2)]
        # make unique
        sum_of_pre_list = set(sum_of_pre_list)
        if search_num in sum_of_pre_list:
            number_list.remove(search_num)
            preamble_list.remove(preamble_list[0])
            preamble_list.append(search_num)
        else:
            return search_num


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')

    preable_list, number_list = convert_input(input_file, 25)
    invalid_number = search_invalid_xmas(preable_list, number_list)

    print("PART ONE:", invalid_number)
