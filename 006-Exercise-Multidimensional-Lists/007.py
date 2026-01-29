def read_matrix():
    n = int(input())
    matrix = []
    for rows in range(n):
        matrix.append([int(el) for el in input().split()])
    return matrix


def read_bomb_coordinates():
    bombs_coordinates = input().split()
    bombs_coordinates_as_tuples = []
    for bomb in bombs_coordinates:
        bomb_coordinates = [int(el) for el in bomb.split(",")]
        bombs_coordinates_as_tuples.append(tuple(bomb_coordinates))

    return bombs_coordinates_as_tuples


def find_bomb_range(matrix, bomb_coordinates):
    r, c = bomb_coordinates
    affected_areas = [
        (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
        (r, c - 1), (r, c + 1),
        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
    ]

    return affected_areas


def attack_square(matrix, coordinates, strength):
    """first checks if the index is in range
    then it reduces the value by the given strength
    finally it returns the updated matrix"""
    r, c = coordinates
    if r not in range(len(matrix)) or c not in range(len(matrix)):
        return matrix

    if matrix[r][c] > 0:
        matrix[r][c] -= strength

    return matrix


def bombs_explode(bombs_coordinates, matrix):
    for bomb in bombs_coordinates:
        bomb_range = find_bomb_range(matrix, bomb)
        bomb_strength = matrix[bomb[0]][bomb[1]]
        if bomb_strength <= 0:
            continue

        for square in bomb_range:
            matrix = attack_square(matrix, square, bomb_strength)
        matrix[bomb[0]][bomb[1]] = 0

    return matrix


def get_alive_cells(matrix):
    alive_cells = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > 0:
                alive_cells.append(matrix[i][j])

    number_alive_cells = len(alive_cells)
    sum_alive_cells = sum(alive_cells)

    return number_alive_cells, sum_alive_cells


def print_result(count, overall_sum, matrix):
    print(f"Alive cells: {count}")
    print(f"Sum: {overall_sum}")
    for line in matrix:
        print(*line, sep=" ")


matrix = read_matrix()
bombs_coordinates = read_bomb_coordinates()
matrix_after_explosions = bombs_explode(bombs_coordinates, matrix)
alive_cells_count, alive_cells_sum = get_alive_cells(matrix_after_explosions)
print_result(alive_cells_count, alive_cells_sum, matrix_after_explosions)
