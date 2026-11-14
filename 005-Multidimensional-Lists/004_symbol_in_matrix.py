def read_matrix(is_test=False):
    if is_test:
        return [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["X", "!", "@"],
        ]

    rows_count = int(input())
    matrix = []
    for row_index in range(rows_count):
        matrix.append(list(input()))

    return matrix


def find_first_occurrence_of_symbol(symbol, matrix):
    rows = len(matrix)
    for row in range(rows):
        if symbol in matrix[row]:
            column = matrix[row].index(symbol)
            return row, column


def print_result(symbol, result):
    if result:
        print(result)
    else:
        print(f"{symbol} does not occur in the matrix")


matrix = read_matrix()
searched_symbol = input()
result = find_first_occurrence_of_symbol(searched_symbol, matrix)
print_result(searched_symbol, result)
