def read_matrix():
    n = int(input().split()[0])

    matrix = []
    for rows in range(n):
        matrix.append(list(input()))

    return matrix


def find_starting_position(matrix):
    position = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "P":
                position = i, j

    return position


def follow_command(matrix, current_position, command):
    r, c = current_position
    matrix[r][c] = "."

    if command == "U":
        r -= 1
    elif command == "D":
        r += 1
    elif command == "L":
        c -= 1
    elif command == "R":
        c += 1

    if r in range(len(matrix)) and c in range(len(matrix[0])):
        if matrix[r][c] == "B":
            global busted
            busted = True
            return r, c

        matrix[r][c] = "P"
    return r, c


def escaped(matrix):
    """checks if the player left the board a.k.a """
    for row in matrix:
        if "P" in row:
            return False

    return True


def player_found_a_bunny(matrix, position):
    r, c = position
    if matrix[r][c] == "B":
        return True

    return False


def find_bunnies(matrix):
    bunnies = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "B":
                bunnies.append((i, j))

    return bunnies


def bunnies_procreate(matrix):
    global busted
    bunnies = find_bunnies(matrix)
    killed = False
    for r, c in bunnies:

        baby_bunnies = [
            [r, c - 1],
            [r + 1, c],
            [r, c + 1],
            [r - 1, c]
        ]

        for row, col in baby_bunnies:
            if row not in range(len(matrix)) or \
                    col not in range(len(matrix[0])):
                continue
            if matrix[row][col] == "P":
                busted = True
                killed = True
                matrix[row][col] = "B"
                busted_coordinates = row, col
            matrix[row][col] = "B"

    if busted and killed:
        return busted, busted_coordinates
    return True, True


def print_result(matrix, coordinates, won=True):
    for row in matrix:
        print(*row, sep="")
    if won:
        print("won: ", end='')
    else:
        print("dead: ", end="")
    print(*coordinates, sep=" ")


matrix = read_matrix()
commands = list(input())
position = find_starting_position(matrix)
busted = False

for move in range(len(commands)):
    command = commands[move]
    new_position = follow_command(matrix, position, command)
    coordinates = bunnies_procreate(matrix)[1]
    if escaped(matrix) and not busted:
        print_result(matrix, position)
        break
    if player_found_a_bunny(matrix, new_position) or busted:
        print_result(matrix, new_position, won=False)
        break
    if busted:
        print_result(matrix, coordinates, won=False)
        break

    position = new_position
