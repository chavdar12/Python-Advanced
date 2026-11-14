ROWS, COLS = 6, 7
EMPTY = "0"
DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1)]  # horizontal, vertical, both diagonals


def create_board(rows=ROWS, cols=COLS):
    return [[EMPTY] * cols for _ in range(rows)]


def drop_piece(board, col, sign):
    """Drops the sign into 0-based column col and returns the row it lands on."""
    if not 0 <= col < len(board[0]):
        raise ValueError(f"Column must be between 1 and {len(board[0])}")
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = sign
            return row
    raise ValueError("This column is full")


def is_winner(board, row, col, sign):
    for dr, dc in DIRECTIONS:
        count = 1
        for direction in (1, -1):
            r, c = row + dr * direction, col + dc * direction
            while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == sign:
                count += 1
                r, c = r + dr * direction, c + dc * direction
        if count >= 4:
            return True
    return False


def is_full(board):
    return all(cell != EMPTY for cell in board[0])


def print_board(board):
    for row in board:
        print(row)


def main():
    board = create_board()
    players = [1, 2]
    turn = 0
    while True:
        player = players[turn % 2]
        try:
            col = int(input(f"Player {player}, please choose a column: ")) - 1
            row = drop_piece(board, col, str(player))
        except ValueError as error:
            print(error)
            continue
        print_board(board)
        if is_winner(board, row, col, str(player)):
            print(f"The winner is player {player}")
            break
        if is_full(board):
            print("It's a draw")
            break
        turn += 1


if __name__ == "__main__":
    main()
