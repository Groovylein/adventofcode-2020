import os


def transform_input(input_file):
    return_list = []
    with open(input_file) as openfile:
        lines = openfile.read()
        for elem in lines.split("\n\n"):
            my_list = []
            elem = elem.replace('\n','')
            for char in elem:
                my_list.append(char) if char not in my_list else my_list
            return_list.append(my_list)
    return return_list


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')

    list_of_lists = transform_input(input_file)
    sum_of_counts = 0
    for list in list_of_lists:
        sum_of_counts += len(list)

    print("PART ONE:", sum_of_counts)
