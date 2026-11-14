DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

n = int(input())
field = [input().split() for _ in range(n)]
bunny = next((r, c) for r in range(n) for c in range(n) if field[r][c] == "B")

best_direction, best_path, best_eggs = None, [], float("-inf")
for direction, (dr, dc) in DIRECTIONS.items():
    r, c = bunny
    path, eggs = [], 0
    while True:
        r, c = r + dr, c + dc
        if not (0 <= r < n and 0 <= c < n) or field[r][c] == "X":
            break
        path.append([r, c])
        eggs += int(field[r][c])
    if path and eggs > best_eggs:
        best_direction, best_path, best_eggs = direction, path, eggs

print(best_direction)
for position in best_path:
    print(position)
print(best_eggs)
