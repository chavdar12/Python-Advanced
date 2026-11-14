groups = input().split("|")
print(*[number for group in reversed(groups) for number in group.split()])
