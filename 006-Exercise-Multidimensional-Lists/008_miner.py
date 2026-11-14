def read_matrix(n):
    matrix = []
    for rows in range(n):
        matrix.append(input().split())

    return matrix


def find_starting_position(matrix):
    starting_position = None
    found_it = False
    for i in range(len(matrix)):
        for j in range(len(matrix)):

            if matrix[i][j] == "s":
                starting_position = (i, j)
                found_it = True
                break
        if found_it:
            break

    return starting_position


def follow_command(matrix, command, position):
    new_position = position
    r, c = position

    if command == "up":
        r -= 1

    elif command == "down":
        r += 1

    elif command == "right":
        c += 1

    elif command == "left":
        c -= 1

    if the_index_is_valid(matrix, (r, c)):
        new_position = r, c

    return new_position


def the_index_is_valid(matrix, indices):
    """checks if the index is valid"""
    row, column = indices
    if row in range(len(matrix)) and column in range(len(matrix)):
        return True

    return False


def check_position(matrix, new_position):
    row, column = new_position
    character = matrix[row][column]

    if character == "c":
        found_coal(matrix, row, column)
    elif character == "e":
        found_end(matrix, row, column)


def found_coal(matrix, row, column):
    global game_over
    matrix[row][column] = "*"
    coals_left = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "c":
                coals_left += 1

    if coals_left == 0:
        game_over = True
        return print(f"You collected all coals! ({row}, {column})")

    return coals_left


def found_end(matrix, row, column):
    global game_over
    game_over = True
    return print(f"Game over! ({row}, {column})")


matrix_size = int(input())
commands = input().split()
matrix = read_matrix(matrix_size)
start_position = find_starting_position(matrix)
new_position = start_position

game_over = False
while commands:
    command = commands.pop(0)
    new_position = follow_command(matrix, command, new_position)
    check_position(matrix, new_position)

    if game_over:
        break

if not game_over:
    coals_left = found_coal(matrix, 0, 0)
    print(f"{coals_left} coals left. ({new_position[0]}, {new_position[1]})")
