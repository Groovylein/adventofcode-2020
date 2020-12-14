import os


def get_adapter_jolts(numbers_list):
    one_jolt_diff = 0
    three_jolt_diff = 0
    diff_jolt = 0
    current_jolt = 1

    max_number = max(numbers_list)
    max_number = max_number + 3
    numbers_list.append(max_number)

    numbers_list.sort()
    # print(numbers_list)

    while True:
        if current_jolt in numbers_list:
            numbers_list.remove(current_jolt)
            if (current_jolt - diff_jolt) == 1:
                one_jolt_diff += 1
            elif (current_jolt - diff_jolt) == 3:
                # print(current_jolt)
                three_jolt_diff += 1

            diff_jolt = current_jolt
            current_jolt += 1

        else:
            current_jolt += 1

        if len(numbers_list) == 0:
            return one_jolt_diff, three_jolt_diff


def create_arrangements(numbers_list):
    numbers_list.sort()

    max_number = max(numbers_list)
    max_number = max_number + 3

    arrangements = [numbers_list]

    for i in numbers_list:
        test_list = numbers_list.copy()
        test_list.remove(i)
        new_list = []
        diff_jolt = 0
        current_jolt = 1
        while True:
            if current_jolt in test_list:
                test_list.remove(current_jolt)
                if (current_jolt - diff_jolt) == 1 or \
                        (current_jolt - diff_jolt) == 3:
                    new_list.append(current_jolt)
                    # print(current_jolt)
                    diff_jolt = current_jolt
                    current_jolt += 1
                else:
                    break
            else:
                current_jolt += 1

            if current_jolt == max_number:
                arrangements.append(new_list)
                break

    print(arrangements)
    return arrangements


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    with open(input_file, "r") as openfile:
        numbers_in_file = [int(n) for n in openfile.read().splitlines()]

    one_jolt, three_jolts = get_adapter_jolts(numbers_in_file.copy())

    print("FIRST PART:", (one_jolt * three_jolts))
