def read_matrix():
    matrix = []
    rows = [int(el) for el in input().split()][0]
    for row in range(rows):
        matrix.append([el for el in input().split()])

    return matrix


def valid_input(action, matrix):
    """Valid if starts with 'swap', is followed by 4 integers,
    and is withing the matrix range."""
    elements = action.split()
    if len(elements) < 5:
        return False

    if not elements[0] == "swap":
        return False

    for char in elements[1:]:
        if not char.isdigit():
            return False

    for el in range(1, 5):
        if not el % 2 == 0:
            if not int(elements[el]) in range(len(matrix)):
                return False
        else:
            if not int(elements[el]) in range(len(matrix[0])):
                return False

    return True


def get_indices(action):
    elements = action.split()
    first_index = elements[1], elements[2]
    second_index = elements[3], elements[4]

    return first_index, second_index


def replace_values(index1, index2, matrix):
    row1, col1 = [int(el) for el in index1]
    row2, col2 = [int(el) for el in index2]
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    return matrix


def print_result(result):
    for line in result:
        print(*line, sep=" ")


matrix = read_matrix()

command = input()
while not command == "END":
    if valid_input(command, matrix):
        first_index, second_index = get_indices(command)
        matrix = replace_values(first_index, second_index, matrix)
        print_result(matrix)
    else:
        print("Invalid input!")

    command = input()
