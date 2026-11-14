from functools import reduce

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,  # the task rounds division down
}

numbers = []
for token in input().split():
    if token in OPERATIONS:
        numbers = [reduce(OPERATIONS[token], numbers)]
    else:
        numbers.append(int(token))

print(numbers[0])
