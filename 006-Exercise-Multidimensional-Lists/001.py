def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ]
    rows = int(input())

    matrix = []
    for row in range(rows):
        matrix.append([int(el) for el in input().split()])

    return matrix


def sum_primary_diagonal(matrix):
    rows = columns = len(matrix)
    sum_diagonal = 0
    for rows in range(rows):
        sum_diagonal += matrix[rows][rows]
    return sum_diagonal


def sum_secondary_diagonal(matrix):
    rows = columns = len(matrix)
    sum_diagonal = 0
    for x in range(rows):
        y = rows - 1 - x
        sum_diagonal += matrix[x][y]
    return sum_diagonal


def find_abs_difference(diagonal1, diagonal2):
    result = abs(diagonal1 - diagonal2)
    return result


def print_result(result):
    print(result)


matrix = read_matrix()
primary_diagonal = sum_primary_diagonal(matrix)
secondary_diagonal = sum_secondary_diagonal(matrix)
result = find_abs_difference(primary_diagonal, secondary_diagonal)
print_result(result)
