r, c = [int(el) for el in input().split()]
matrix = [[chr(97 + row) + chr(97 + row + column) + chr(97 + row) for column in range(c)] for row in range(r)]
[print(*row) for row in matrix]
