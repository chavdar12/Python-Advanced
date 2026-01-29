import sys


def read_matrix():
    matrix = []
    rows = [int(el) for el in input().split()][0]
    for row in range(rows):
        matrix.append([int(el) for el in input().split()])

    return matrix


def get_sub_matrix(row, column, size, matrix):
    sub_matrix = []
    for r in range(row, row + size):
        row_of_sub_matrix = []
        for c in range(column, column + size):
            row_of_sub_matrix.append(matrix[r][c])
        sub_matrix.append(row_of_sub_matrix)

    return sub_matrix


def get_sum_and_initial_index(matrix):
    SUB_MATRIX_SIZE = 3
    max_sum = -sys.maxsize
    max_sub_matrix = []
    for row in range(len(matrix) - SUB_MATRIX_SIZE + 1):
        for col in range(len(matrix[0]) - SUB_MATRIX_SIZE + 1):
            sub_matrix = get_sub_matrix(row, col, SUB_MATRIX_SIZE, matrix)
            sub_matrix_sum = matrix_sum(sub_matrix)
            if sub_matrix_sum > max_sum:
                max_sum = sub_matrix_sum
                max_sub_matrix = sub_matrix

    return max_sum, max_sub_matrix


def matrix_sum(matrix):
    rows = len(matrix)
    matrix_sum = 0
    for row in range(rows):
        matrix_sum += sum(matrix[row])

    return matrix_sum


def print_result(result, matrix):
    print(f"Sum = {result}")
    for line in matrix:
        print(*line, sep=" ")


matrix = read_matrix()
max_sum_sub_matrix, sub_matrix = get_sum_and_initial_index(matrix)
print_result(max_sum_sub_matrix, sub_matrix)
