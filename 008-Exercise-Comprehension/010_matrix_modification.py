def read_matrix(dimension):
    matrix = [[int(j) for j in input().split()] for i in range(dimension)]

    return matrix


def indices_are_valid(row, column, matrix):
    return True \
        if row in range(len(matrix)) and column in range(len(matrix[0])) \
        else False


def increase_number_at_coordinates(matrix, command):
    row, col, value = [int(el) for el in command.split()[1:]]

    if not indices_are_valid(row, col, matrix):
        return print("Invalid coordinates")

    matrix[row][col] += value


def decrease_number_at_coordinates(matrix, command):
    row, col, value = [int(el) for el in command.split()[1:]]

    if not indices_are_valid(row, col, matrix):
        return print("Invalid coordinates")

    matrix[row][col] -= value


def manipulate_matrix(matrix):
    command = input()
    while not command == "END":
        if "Add" in command:
            increase_number_at_coordinates(matrix, command)

        elif "Subtract" in command:
            decrease_number_at_coordinates(matrix, command)

        command = input()


def print_matrix(matrix):
    [print(*row) for row in matrix]


dimension = int(input())
matrix = read_matrix(dimension)
manipulate_matrix(matrix)
print_matrix(matrix)
