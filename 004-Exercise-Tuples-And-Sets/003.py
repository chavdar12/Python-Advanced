def input_to_list(number_of_lines):
    my_input = []
    for _ in range(number_of_lines):
        my_input.append(input())

    return my_input


def input_to_set(elements):
    my_input = set()
    for element in elements:
        if " " in element:
            for el in element.split():
                my_input.add(el)
        else:
            my_input.add(element)
    return my_input


def print_result(result):
    if result:
        print(*set(result), sep="\n")


n = int(input())
elements = input_to_list(n)
set_of_unique_elements = input_to_set(elements)
print_result(set_of_unique_elements)
