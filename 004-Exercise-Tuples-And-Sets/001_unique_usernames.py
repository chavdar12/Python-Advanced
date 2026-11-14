def input_to_list(number_of_lines):
    my_input = []
    for _ in range(number_of_lines):
        my_input.append(input())

    return my_input


def print_result(result):
    print(*set(result), sep="\n")


n = int(input())
names = input_to_list(n)
print_result(names)
