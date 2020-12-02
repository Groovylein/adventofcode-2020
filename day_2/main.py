import os

def password_validation_part_one(condition, password):
    condition_ocurrence, condition_value = condition.split()
    start_occurence, stop_occurence = condition_ocurrence.split("-")
    if int(start_occurence) <= int(password.count(condition_value)) <= int(stop_occurence):
        return True
    else:
        return False

def password_validation_part_two(condition, password):
    condition_ocurrence, condition_value = condition.split()
    first_occurence, second_occurence = condition_ocurrence.split("-")
    first = int(first_occurence) - 1
    second = int(second_occurence) - 1
    if condition_value in password[first]:
        if condition_value in password[second]:
            return False
        else:
            return True
    else:
        if condition_value in password[second]:
            return True
        else:
            return False


if __name__ == "__main__":
    input_condition_list = []
    input_password_list = []
    counter_valid_part_one = 0
    counter_valid_part_two = 0
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    with open(input_file, "r") as openfile:
        for line in openfile:
            line = line.strip()
            # print(line)
            input_condition, input_password = line.split(":")
            if password_validation_part_one(input_condition, input_password.strip()) is True:
                counter_valid_part_one += 1
            if password_validation_part_two(input_condition, input_password.strip()) is True:
                counter_valid_part_two += 1
    
    print("ANSWER PART ONE:", counter_valid_part_one)
    print("ANSWER PART TWO:", counter_valid_part_two)