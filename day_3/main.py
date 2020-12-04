import os


def read_input(file_path):
    return_list = []
    with open(file_path, "r") as openfile:
        for line in openfile:
            return_list.append(list(line.strip()))
    return return_list


def toboggan_run(geo_list, column, row):
    # right 3, down 1
    index_row = 0
    index_column = 0
    tree_counter = 0
    for i in geo_list:
        # print("TREE:", tree_counter)
        index_column += column
        index_row += row
        try:
            if 0 <= index_column < len(geo_list[index_row]):
                # print(geo_list[index_row][index_column])
                if geo_list[index_row][index_column] == "#":
                    tree_counter += 1
            else:
                index_column -= len(geo_list[index_row])
                # print(geo_list[index_row][index_column])
                if geo_list[index_row][index_column] == "#":
                    tree_counter += 1
        except:
            pass
    return tree_counter


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    input_as_list = read_input(input_file)

    toboggan_1 = toboggan_run(input_as_list, 1, 1)
    toboggan_2 = toboggan_run(input_as_list, 3, 1)
    toboggan_3 = toboggan_run(input_as_list, 5, 1)
    toboggan_4 = toboggan_run(input_as_list, 7, 1)
    toboggan_5 = toboggan_run(input_as_list, 1, 2)
    multiplied = toboggan_1 * toboggan_2 * toboggan_3 * toboggan_4 * toboggan_5
    print(multiplied)
