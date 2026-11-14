from collections import deque

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b else 0,
}

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())
total = 0

while bees and nectar:
    collected = nectar.pop()
    if collected < bees[0]:
        continue
    total += abs(OPERATIONS[symbols.popleft()](bees.popleft(), collected))

print(f"Total honey made: {int(total) if total == int(total) else total}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
