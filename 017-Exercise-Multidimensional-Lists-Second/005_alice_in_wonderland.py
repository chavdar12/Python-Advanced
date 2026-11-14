DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

n = int(input())
field = [input().split() for _ in range(n)]
r, c = next((r, c) for r in range(n) for c in range(n) if field[r][c] == "A")
field[r][c] = "*"
tea = 0

while tea < 10:
    dr, dc = DIRECTIONS[input()]
    r, c = r + dr, c + dc
    if not (0 <= r < n and 0 <= c < n):
        break
    cell = field[r][c]
    field[r][c] = "*"
    if cell == "R":
        break
    if cell.isdigit():
        tea += int(cell)

print("She did it! She went to the party." if tea >= 10 else "Alice didn't make it to the tea party.")
for row in field:
    print(*row)
