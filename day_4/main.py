import os


def transform_data(input_data_file):
    return_list = []
    dict_append = {}
    with open(input_data_file) as openfile:
        lines = openfile.read()
        for elem in lines.split("\n\n"):
            passport_list = elem.split()
            for passport in passport_list:
                key, value = passport.split(":")
                dict_append[key] = value
            return_list.append(dict_append)
            dict_append = {}
    return return_list


def check_data(passports_as_list):
    # byr
    # iyr
    # eyr
    # hgt
    # hcl
    # ecl
    # pid
    valid_passports = 0
    validatikon_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports_as_list:
        for key in validatikon_keys:
            if key not in passport:
                break
        else:
            # Continue if the inner loop wasn't broken.
            valid_passports += 1
            continue

    return valid_passports


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    passports_as_list = transform_data(input_file)
    print("First Part:", check_data(passports_as_list))
