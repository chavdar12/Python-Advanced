def read_input():
    return [float(el) for el in input().split()]


def count_num_occurrences(list_numbers):
    occurrences = {}
    for num in list_numbers:
        if num not in occurrences:
            occurrences[num] = 0
        occurrences[num] += 1

    return occurrences


def print_result(dictionary_numbers):
    for number, instances in dictionary_numbers.items():
        print(f"{number} - {instances} times")


numbers = read_input()
numbers_occurrences = count_num_occurrences(numbers)
print_result(numbers_occurrences)
