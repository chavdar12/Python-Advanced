first = set(map(int, input().split()))
second = set(map(int, input().split()))
sequences = {"First": first, "Second": second}

for _ in range(int(input())):
    command = input().split()
    if command[0] == "Check":
        print(first <= second or second <= first)
        continue
    action, which, *numbers = command
    target = sequences[which]
    if action == "Add":
        target.update(map(int, numbers))
    else:
        target.difference_update(map(int, numbers))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
