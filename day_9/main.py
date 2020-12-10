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


def break_xmas(input_list, search_number):
    outer_loop = True
    inner_loop = True

    while outer_loop:
        sum_list = []
        idx = 0
        sum_list.append(input_list[idx])
        idx = (idx + 1) % len(input_list)
        sum_list.append(input_list[idx])

        while inner_loop:
            sum_of_list = sum(sum_list)
            if sum_of_list == search_number:
                return tuple(sum_list)
            elif sum_of_list > search_number:
                inner_loop = False
            else:
                idx = (idx + 1) % len(input_list)
                sum_list.append(input_list[idx])

        input_list.remove(input_list[0])
        inner_loop = True


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')

    p_list, n_list = convert_input(input_file, 25)
    invalid_number = search_invalid_xmas(p_list.copy(), n_list.copy())

    print("PART ONE:", invalid_number)

    input_list = p_list + n_list
    broken_tuple = break_xmas(input_list, invalid_number)

    max_n = max(broken_tuple)
    min_n = min(broken_tuple)

    print("PART TWO", max_n + min_n)
