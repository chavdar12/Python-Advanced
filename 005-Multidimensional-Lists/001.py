def read_a_matrix(test=False):
    if test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]

    row_count, column_count = [int(el) for el in input().split(", ")]
    matrix = []
    for row_index in range(row_count):
        row = [int(el) for el in input().split(", ")]
        matrix.append(row)

    return matrix


matrix = read_a_matrix()

sum_of_nums = 0
for row_index in range(len(matrix)):
    sum_of_nums += sum(matrix[row_index])

print(sum_of_nums)
print(matrix)
