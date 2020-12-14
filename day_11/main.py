import copy
import os


def read_input(file_path):
    return_list = []
    with open(file_path, "r") as openfile:
        for line in openfile:
            return_list.append(list(line.strip()))
    return return_list


def get_adjacent(input_as_list, line_i, row_i):
    # a b c
    # h X d
    # g f e
    try:
        i = line_i - 1
        j = row_i - 1
        if i >= 0 and j >= 0:
            a = input_as_list[i][j]
        else:
            a = ""
    except:
        a = ""
    try:
        i = line_i - 1
        j = row_i
        if i >= 0 and j >= 0:
            b = input_as_list[i][j]
        else:
            b = ""
    except:
        b = ""
    try:
        i = line_i - 1
        j = row_i + 1
        if i >= 0 and j >= 0:
            c = input_as_list[i][j]
        else:
            c = ""
    except:
        c = ""
    try:
        i = line_i
        j = row_i + 1
        if i >= 0 and j >= 0:
            d = input_as_list[i][j]
        else:
            d = ""
    except:
        d = ""
    try:
        i = line_i + 1
        j = row_i - 1
        if i >= 0 and j >= 0:
            e = input_as_list[i][j]
        else:
            e = ""
    except:
        e = ""
    try:
        i = line_i + 1
        j = row_i
        if i >= 0 and j >= 0:
            f = input_as_list[i][j]
        else:
            f = ""
    except:
        f = ""
    try:
        i = line_i + 1
        j = row_i + 1
        if i >= 0 and j >= 0:
            g = input_as_list[i][j]
        else:
            g = ""
    except:
        g = ""
    try:
        i = line_i
        j = row_i - 1
        if i >= 0 and j >= 0:
            h = input_as_list[i][j]
        else:
            h = ""
    except:
        h = ""
    return [a, b, c, d, e, f, g, h]


def do_iteration(input_as_list):
    return_list = copy.deepcopy(input_as_list)
    for line_i in range(len(input_as_list)):
        for row_i in range(len(input_as_list[line_i])):
            if input_as_list[line_i][row_i] is not ".":
                adjacent_list = get_adjacent(input_as_list, line_i, row_i)
                count_occupied = adjacent_list.count("#")
                for adjacent in adjacent_list:
                    if input_as_list[line_i][row_i] is "L" and \
                            adjacent is not "#":
                        return_list[line_i][row_i] = "#"
                    if adjacent is "#" and count_occupied >= 4:
                        return_list[line_i][row_i] = "L"

    return return_list


def search_stabilization(input_as_list):
    prev_list = copy.deepcopy(input_as_list)
    while True:
        next_list = do_iteration(copy.deepcopy(prev_list))
        if next_list == prev_list:
            return next_list
        else:
            prev_list = next_list


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    input_as_list = read_input(input_file)
