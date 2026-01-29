rows = int(input())

matrix = [
    int(j)
    for row in range(rows)
    for j in input().split(", ")
]
print(matrix)
