import os


def get_row_column(pass_number):
    row_indicator = pass_number[0:-3]
    column_indicator = pass_number[-3:]
    return_row = range(0, 128)
    return_column = range(0,8)
    for char_row in row_indicator:
        row_length = len(return_row)
        middle_row_index = row_length // 2
        if char_row == "F":
            return_row = return_row[:middle_row_index]
        elif char_row == "B":
            return_row = return_row[middle_row_index:]

    for char_column in column_indicator:
        column_length = len(return_column)
        middle_column_index = column_length // 2
        if char_column == "L":
            return_column = return_column[:middle_column_index]
        elif char_column == "R":
            return_column = return_column[middle_column_index:]

    return return_row[0], return_column[0]


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    list_of_calculations = []
    with open(input_file, "r") as openfile:
        for line in openfile:
            line = line.strip()
            row, column = get_row_column(line)
            calc = (row * 8) + column
            list_of_calculations.append(calc)
    print("PART ONE:",max(list_of_calculations))
