def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

    rows_count = int(input())
    matrix = []
    for row_index in range(rows_count):
        matrix.append([int(el) for el in input().split(" ")])

    return matrix


def find_primary_diagonal(the_matrix):
    sum_primary_diagonal = 0
    rows = len(the_matrix)

    for x in range(rows):
        sum_primary_diagonal += the_matrix[x][x]

    return sum_primary_diagonal


def find_secondary_diagonal(the_matrix):
    sum_secondary_diagonal = 0
    rows = len(the_matrix)

    for x in range(rows):
        y = rows - 1 - x
        sum_secondary_diagonal += the_matrix[x][y]

    return sum_secondary_diagonal


def print_result(result):
    print(result)


matrix = read_matrix()
result = find_primary_diagonal(matrix)
result = find_secondary_diagonal(matrix)

print_result(result)
