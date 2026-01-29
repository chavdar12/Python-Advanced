def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

    rows_count, columns_count = [int(el) for el in input().split(", ")]
    matrix = []
    for row_index in range(rows_count):
        matrix.append([int(el) for el in input().split(" ")])

    return matrix


def sum_each_matrix_column(the_matrix):
    for each_columns in range(len(the_matrix[0])):
        sum_elements = 0
        for row in range(len(the_matrix)):
            sum_elements += the_matrix[row][each_columns]
        print(sum_elements)


matrix = read_matrix()
sum_each_matrix_column(matrix)
