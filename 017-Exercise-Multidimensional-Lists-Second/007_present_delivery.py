DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

presents = int(input())
n = int(input())
field = [input().split() for _ in range(n)]
r, c = next((r, c) for r in range(n) for c in range(n) if field[r][c] == "S")
nice_total = sum(row.count("V") for row in field)
nice_given = 0

command = input()
while command != "Christmas morning":
    dr, dc = DIRECTIONS[command]
    field[r][c] = "-"
    r, c = r + dr, c + dc
    if field[r][c] == "V":
        presents -= 1
        nice_given += 1
    elif field[r][c] == "C":
        for ddr, ddc in DIRECTIONS.values():
            kid = field[r + ddr][c + ddc]
            if kid in ("V", "X") and presents:
                presents -= 1
                nice_given += kid == "V"
                field[r + ddr][c + ddc] = "-"
    field[r][c] = "S"
    if presents == 0:
        break
    command = input()

nice_left = nice_total - nice_given
if presents == 0 and nice_left:
    print("Santa ran out of presents!")
for row in field:
    print(*row)
if nice_left == 0:
    print(f"Good job, Santa! {nice_total} happy nice kid/s.")
else:
    print(f"No presents for {nice_left} nice kid/s.")
