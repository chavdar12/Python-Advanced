def read_matrix():
    n = int(input())
    matrix = []
    for rows in range(n):
        matrix.append([])
        row = input()
        for char in row:
            matrix[-1].append(char)

    return matrix


def update_dictionary(dicky, key):
    if key not in dicky:
        dicky[key] = 0
    dicky[key] += 1

    return dicky


def find_all_knights(matrix):
    knights = []
    for r in range(len(matrix)):
        for c in range(len(matrix)):

            current_char = matrix[r][c]
            if current_char == "K":
                knights.append((r, c))

    return knights


def find_attacking_knights(matrix, all_knights):
    attacking_knights = {}
    for row, col in all_knights:

        attacked_positions = [
            (row - 1, col - 2),
            (row - 2, col - 1),
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
        ]

        for attacked_row, attacked_col in attacked_positions:
            if attacked_row not in range(len(matrix)):
                continue
            if attacked_col not in range(len(matrix)):
                continue

            if matrix[attacked_row][attacked_col] == "K":
                attacking_knights = update_dictionary(attacking_knights, (row, col))

    return attacking_knights


def remove_attacking_knights(matrix, attacking_knights):
    """removes attacking knights"""
    deletion = 0
    while attacking_knights():

        most_aggressive_knight = "", ""
        top_value = None
        for coordinates, value in attacking_knights.items():
            if top_value is None or value > top_value:
                top_value = value
                most_aggressive_knight = coordinates
        row, column = most_aggressive_knight
        matrix[row][column] = "0"
        deletion += 1
        attacking_knights = find_attacking_knights(matrix, attacking_knights)

    return deletion


def find_most_aggressive_knight(attacking_knights):
    most_aggressive_knight_coordinates = None
    aggression = None

    for coordinates, value in attacking_knights.items():

        if aggression is None or value > aggression:
            aggression = value
            most_aggressive_knight_coordinates = coordinates

    return most_aggressive_knight_coordinates


def main():
    matrix = read_matrix()
    knights = find_all_knights(matrix)
    attacking_knights = find_attacking_knights(matrix, knights)

    removed_knights = 0

    while attacking_knights:
        most_aggressive_knight_coordinates = find_most_aggressive_knight(attacking_knights)

        row, column = most_aggressive_knight_coordinates
        matrix[row][column] = "0"
        knights.remove((row, column))
        removed_knights += 1

        attacking_knights = find_attacking_knights(matrix, knights)

    print(removed_knights)


main()
