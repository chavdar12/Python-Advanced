def input_to_list(number_of_lines):
    my_input = []
    for _ in range(number_of_lines):
        my_input.append(input())

    return my_input


n = int(input())

names = input_to_list(n)
unique_names = set(names)
print(*unique_names, sep='\n')
