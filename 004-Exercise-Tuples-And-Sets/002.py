def input_to_set(number_of_lines):
    my_input = set()
    for _ in range(number_of_lines):
        my_input.add(input())

    return my_input


def print_result(result):
    if result:
        print(*set(result), sep="\n")


length_first_set, length_second_set = map(int, input().split())

numbers_first_set = input_to_set(length_first_set)
numbers_second_set = input_to_set(length_second_set)

numbers_in_both_sets = numbers_first_set.intersection(numbers_second_set)
print_result(numbers_in_both_sets)
