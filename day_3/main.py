import os


def read_input(file_path):
    return_list = []
    with open(file_path, "r") as openfile:
        for line in openfile:
            return_list.append(list(line.strip()))
    return return_list


def toboggan_run(geo_list):
    # right 3, down 1
    index_row = 0
    index_column = 0
    tree_counter = 0
    for row in geo_list:
        # print("TREE:", tree_counter)
        index_column += 3
        index_row += 1
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

    print(toboggan_run(input_as_list))
