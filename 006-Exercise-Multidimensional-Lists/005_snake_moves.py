def read_matrix():
    matrix = []
    rows, columns = [int(el) for el in input().split()]
    for row in range(rows):
        matrix.append([] * columns)

    return matrix, rows, columns


def print_result(result: list):
    for row in result:
        print(*row, sep="")


def reverse_every_second_row(matrix):
    for row in range(len(matrix)):
        if row % 2 == 1:
            matrix[row] = reversed(matrix[row])

    return matrix


empty_matrix, rows, columns = read_matrix()
snek = input()

position = 0
for r in range(rows):
    for c in range(columns):
        building_block = snek[position]
        empty_matrix[r].append(building_block)
        position += 1
        if position == len(snek):
            position = 0

snek_matrix = reverse_every_second_row(empty_matrix)
print_result(snek_matrix)
