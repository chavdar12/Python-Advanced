def print_result(diagonal1, diagonal2):
    print(f'First diagonal: {", ".join(list(map(str, diagonal1)))}. Sum: {sum(diagonal1)}')
    print(f'Second diagonal: {", ".join(list(map(str, diagonal2)))}. Sum: {sum(diagonal2)}')


dimensions = int(input())
matrix = [[int(j) for j in input().split(", ")] for i in range(dimensions)]
primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
print_result(primary_diagonal, second_diagonal)
