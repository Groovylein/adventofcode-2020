import os


def transform_input(input_file):
    return_list_part_one = []
    return_list_part_two = []
    with open(input_file) as openfile:
        lines = openfile.read()
        for elem in lines.split("\n\n"):
            return_list_part_one.append(part_one(elem))
            return_list_part_two.append(part_two(elem))
    return return_list_part_one, return_list_part_two


def part_one(elem):
    my_list = []
    elem = elem.replace('\n', '')
    for char in elem:
        my_list.append(char) if char not in my_list else my_list
    return my_list


def part_two(elem):
    people_answered = len(elem.splitlines())
    my_list = []
    elem_oneline = elem.replace('\n', '')
    for char in elem_oneline:
        if elem_oneline.count(char) == people_answered:
            my_list.append(char) if char not in my_list else my_list
    return my_list


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')

    list_of_lists_part_one, list_of_lists_part_two = transform_input(input_file)
    sum_of_counts = 0
    for list in list_of_lists_part_one:
        sum_of_counts += len(list)

    print("PART ONE:", sum_of_counts)

    sum_of_counts = 0
    for list in list_of_lists_part_two:
        sum_of_counts += len(list)

    print("PART TWO:", sum_of_counts)
