import os

def password_validation(condition, password):
    condition_ocurrence, condition_value = condition.split()
    start_occurence, stop_occurence = condition_ocurrence.split("-")
    if int(start_occurence) <= int(password.count(condition_value)) <= int(stop_occurence):
        return True
    else:
        return False


if __name__ == "__main__":
    input_condition_list = []
    input_password_list = []
    counter_valid = 0
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    with open(input_file, "r") as openfile:
        for line in openfile:
            line = line.strip()
            # print(line)
            input_condition, input_password = line.split(":")
            if password_validation(input_condition, input_password) is True:
                counter_valid += 1
    
    print("ANSWER PART ONE:", counter_valid)