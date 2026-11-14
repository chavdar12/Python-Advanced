SIZE = 7
MULTIPLIERS = {"D": 2, "T": 3}

players = input().split(", ")
board = [input().split() for _ in range(SIZE)]
scores = [501, 501]
throws = [0, 0]
current = 0

while True:
    r, c = map(int, input().strip("()").split(", "))
    throws[current] += 1
    if 0 <= r < SIZE and 0 <= c < SIZE:
        cell = board[r][c]
        if cell == "B":
            break
        if cell in MULTIPLIERS:
            edges = int(board[r][0]) + int(board[r][-1]) + int(board[0][c]) + int(board[-1][c])
            scores[current] -= edges * MULTIPLIERS[cell]
        else:
            scores[current] -= int(cell)
        if scores[current] <= 0:
            break
    current = 1 - current

print(f"{players[current]} won the game with {throws[current]} throws!")
