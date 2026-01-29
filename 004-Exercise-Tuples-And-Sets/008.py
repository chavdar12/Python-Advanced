def input_to_list(number_of_lines):
    my_input = []
    for _ in range(number_of_lines):
        my_input.append(input())

    return my_input


def get_ascii_value(names):
    odd_set = set()
    even_set = set()
    for each_name in range(0, len(names)):
        final_num = sum([ord(char) for char in names[each_name]]) // (each_name + 1)

        if final_num % 2 == 0:
            even_set.add(final_num)
        else:
            odd_set.add(final_num)

    return odd_set, even_set


def print_result(odd, even):
    if sum(odd) == sum(even):
        print(*odd.union(even), sep=", ")
    elif sum(odd) > sum(even):
        print(*odd.difference(even), sep=", ")
    elif sum(odd) < sum(even):
        print(*even.symmetric_difference(odd), sep=", ")


n = int(input())

names = input_to_list(n)
odd_nums_set, even_nums_set = get_ascii_value(names)
print_result(odd_nums_set, even_nums_set)
