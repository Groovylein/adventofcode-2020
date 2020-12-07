import os
import re


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
            if check_hair(passport["hcl"]) and \
                    check_eye(passport["ecl"]) and \
                    check_pid(passport["pid"]) and \
                    check_height(passport["hgt"]) and \
                    check_between(1920, 2002, passport["byr"]) and \
                    check_between(2010, 2020, passport["iyr"]) and \
                    check_between(2020, 2030, passport["eyr"]):
                valid_passports += 1
            continue

    return valid_passports


def check_between(a, b, check_value):
    if a <= int(check_value) <= b:
        return True
    else:
        print("Invalid", check_value)
        return False


def check_height(hgt):
    try:
        temp = re.compile("([0-9]+)([a-z]+)")
        number, unit = temp.match(hgt).groups()
        if unit == "in":
            if 59 <= int(number) <= 76:
                return True
        elif unit == "cm":
            if 150 <= int(number) <= 193:
                return True
        print("Invalid Height", hgt)
        return False
    except:
        print("Invalid Height", hgt)
        return False


def check_hair(hcl):
    if re.search(r"^#([0-9a-f]{6})", hcl):
        return True
    print("Invalid Hair", hcl)
    return False


def check_eye(ecl):
    valid_eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in valid_eye_color:
        return True
    print("Invalid EYE", ecl)
    return False


def check_pid(pid):
    if re.search(r"^([0-9]{9}$)", pid):
        return True
    print("Invalid PID", pid)
    return False


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    passports_as_list = transform_data(input_file)
    print("Valid Passports", check_data(passports_as_list))
