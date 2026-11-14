from math import ceil

SIGNS = ("X", "O")


def create_board():
    return [[" "] * 3 for _ in range(3)]


def position_to_cell(position):
    """Maps 1-9 (left to right, top to bottom) to (row, col)."""
    return ceil(position / 3) - 1, (position - 1) % 3


def place(board, position, sign):
    if not 1 <= position <= 9:
        raise ValueError("Choose a number between 1 and 9")
    row, col = position_to_cell(position)
    if board[row][col] != " ":
        raise ValueError("This space is already taken")
    board[row][col] = sign


def check_if_won(board, sign):
    lines = board + [list(col) for col in zip(*board)]
    lines += [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    return any(all(cell == sign for cell in line) for line in lines)


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def draw_board(board):
    for row in board:
        print(f"| {' | '.join(row)} |")


def setup():
    player_one = input("Player one name: ")
    player_two = input("Player two name: ")
    sign = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()
    while sign not in SIGNS:
        sign = input("The sign can only be 'X' or 'O': ").upper()
    other_sign = SIGNS[1 - SIGNS.index(sign)]
    print("This is the numeration of the board:")
    draw_board([[str(r * 3 + c + 1) for c in range(3)] for r in range(3)])
    print(f"{player_one} starts first!")
    return [player_one, sign], [player_two, other_sign]


def main():
    current, other = setup()
    board = create_board()
    while True:
        try:
            place(board, int(input(f"{current[0]} choose a free position [1-9]: ")), current[1])
        except ValueError as error:
            print(error)
            continue
        draw_board(board)
        if check_if_won(board, current[1]):
            print(f"{current[0]} won!")
            break
        if is_full(board):
            print("Draw!")
            break
        current, other = other, current


if __name__ == "__main__":
    main()
