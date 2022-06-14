def read_matrix(is_test=False):
    if is_test:
        return [
            ["A", "B", "B", "D"],
            ["E", "B", "B", "B"],
            ["I", "J", "B", "B"],
        ]

    matrix = []
    rows, cols = [int(el) for el in input().split()]
    for row in range(rows):
        matrix.append(input().split())

    return matrix


def get_sub_matrix(row, column, size, matrix):
    symbol = []

    for each_row in range(row, row + size):
        for each_col in range(column, column + size):
            symbol.append(matrix[each_row][each_col])

    return symbol


def sub_matrices_with_same_elements_count(matrix):
    SUB_MATRIX_SIZE = 2
    count = 0
    for start_row in range(len(matrix) - SUB_MATRIX_SIZE + 1):
        for start_col in range(len(matrix[0]) - SUB_MATRIX_SIZE + 1):
            small_matrix = get_sub_matrix(start_row, start_col, SUB_MATRIX_SIZE, matrix)
            count += check_if_all_elements_are_the_same(small_matrix)

    return count


def check_if_all_elements_are_the_same(glist: list):
    if glist.count(glist[0]) == 4:
        return True

    return False


matrix = read_matrix()
result = sub_matrices_with_same_elements_count(matrix)
print(result)
