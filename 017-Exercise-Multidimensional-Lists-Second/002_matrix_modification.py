n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input()
while command != "END":
    action, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if 0 <= row < n and 0 <= col < len(matrix[row]):
        matrix[row][col] += value if action == "Add" else -value
    else:
        print("Invalid coordinates")
    command = input()

for row in matrix:
    print(*row)
