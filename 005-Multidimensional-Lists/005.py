import sys


def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]

    rows_count, columns_count = [int(el) for el in input().split(", ")]
    matrix = []
    for row_index in range(rows_count):
        matrix.append([int(el) for el in input().split(", ")])

    return matrix


def sub_matrix_sum_and_coordinates(matrix):
    max_sum = -sys.maxsize
    first_index_position = 0
    second_index_position = 0
    third_index_position = 0
    fourth_index_position = 0

    rows = len(matrix)
    columns = len(matrix[0])
    for row_index in range(rows - 1):
        for column_index in range(columns - 1):
            first_num = matrix[row_index][column_index]
            second_num = matrix[row_index][column_index + 1]
            third_num = matrix[row_index + 1][column_index]
            fourth_num = matrix[row_index + 1][column_index + 1]

            total_sum = first_num + second_num + third_num + fourth_num

            if total_sum > max_sum:
                max_sum = total_sum
                first_index_position = first_num

                second_index_position = second_num
                third_index_position = third_num
                fourth_index_position = fourth_num

    return (first_index_position, second_index_position, third_index_position, fourth_index_position), max_sum


def print_result(result):
    coordinates, max_sum = result
    first, second, third, fourth = coordinates
    print(first, second, ' ')
    print(third, fourth, " ")
    print(max_sum)


matrix = read_matrix()
result = sub_matrix_sum_and_coordinates(matrix)
print_result(result)
