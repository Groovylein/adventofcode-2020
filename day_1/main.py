def find_two_numbers(number_list: list) -> tuple:
    search_sum = 2020
    for number in number_list:
        number_list.remove(number)
        remaining = search_sum - number
        if remaining in number_list:
            return (number, remaining)

def find_three_numbers(number_list: list) -> tuple:
    return (0,0,0)

if __name__ == "__main__":
    with open("input.txt", "r") as openfile:
        numbers_in_file = [int(n) for n in openfile.read().splitlines()]
    # print(numbers_in_file)
    number_a1, number_b1 = find_two_numbers(numbers_in_file)
    # print(number_a, number_b)
    print("ANSWER PART ONE:",number_a1 * number_b1)

    number_a2, number_b2, number_c2 = find_three_numbers(numbers_in_file)
    print(number_a2, number_b2, number_c2)