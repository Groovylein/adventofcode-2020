import os


def get_loop(input_file):
    acc = 0
    index = 0
    index_passed = []
    with open(input_file, "r") as openfile:
        operations = openfile.read().splitlines()
    while index not in index_passed:
        op = operations[index]
        activity, value = op.split()
        if activity == "nop":
            index_passed.append(index)
            index += 1
        elif activity == "acc":
            acc += int(value)
            index_passed.append(index)
            index += 1
        elif activity == "jmp":
            index_passed.append(index)
            index += int(value)
    return acc


def fix_loop(input_file):
    acc = 0
    index = 0
    index_passed = []
    changed_index = 0
    with open(input_file, "r") as openfile:
        operations = openfile.read().splitlines()
    while index not in index_passed:
        try:
            op = operations[index]
            activity, value = op.split()
            if activity == "nop":
                index_passed.append(index)
                index += 1
            elif activity == "acc":
                acc += int(value)
                index_passed.append(index)
                index += 1
            elif activity == "jmp":
                index_passed.append(index)
                if int(value) < 0 and changed_index == 0:
                    index += 1
                else:
                    index += int(value)
        except:
            return acc
    return acc


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')

    part_one_acc = get_loop(input_file)

    print("PART ONE:", part_one_acc)

    part_two_acc = fix_loop(input_file)

    print("PART TWO:", part_two_acc)
