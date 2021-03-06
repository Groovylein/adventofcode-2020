import os

def find_two_numbers(number_list: list) -> tuple:
    search_sum = 2020
    for number in number_list:
        # number_list.remove(number)
        remaining = search_sum - number
        if remaining in number_list:
            return (number, remaining)

def find_three_numbers(number_list: list) -> tuple:
    search_sum = 2020
    number_list.sort()
    for number in number_list:
        # number_list.remove(number)
        if len(number_list) > 0:
            next_number = number_list[0]
            intermediate_number = number + next_number
            if intermediate_number <= search_sum:
                remaining = search_sum - intermediate_number
                if remaining in number_list:
                    return (number,next_number,remaining)
    return (0,0,0)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'input.txt')
    with open(input_file, "r") as openfile:
        numbers_in_file = [int(n) for n in openfile.read().splitlines()]
    # print(numbers_in_file)
    number_a1, number_b1 = find_two_numbers(numbers_in_file[:])
    # print(number_a1, number_b1)
    print("ANSWER PART ONE:",number_a1 * number_b1)
    number_a2, number_b2, number_c2 = find_three_numbers(numbers_in_file[:])
    # print(number_a2, number_b2, number_c2)
    print("ANSWER PART TWO:",number_a2 * number_b2 * number_c2)