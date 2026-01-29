list_integers = list(map(int, input().split()))
stored_numbers = []

while list_integers:
    stored_numbers.append(list_integers.pop())

print(*stored_numbers)
