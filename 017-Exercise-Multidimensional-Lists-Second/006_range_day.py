DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
SIZE = 5

field = [input().split() for _ in range(SIZE)]
r, c = next((r, c) for r in range(SIZE) for c in range(SIZE) if field[r][c] == "A")
targets = sum(row.count("x") for row in field)
hit = []

for _ in range(int(input())):
    action, direction, *steps = input().split()
    dr, dc = DIRECTIONS[direction]
    if action == "move":
        nr, nc = r + dr * int(steps[0]), c + dc * int(steps[0])
        if 0 <= nr < SIZE and 0 <= nc < SIZE and field[nr][nc] == ".":
            field[r][c], field[nr][nc] = ".", "A"
            r, c = nr, nc
        continue

    sr, sc = r + dr, c + dc
    while 0 <= sr < SIZE and 0 <= sc < SIZE:
        if field[sr][sc] == "x":
            field[sr][sc] = "."
            hit.append([sr, sc])
            break
        sr, sc = sr + dr, sc + dc
    if len(hit) == targets:
        break

if len(hit) == targets:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets - len(hit)} targets left.")
for position in hit:
    print(position)
