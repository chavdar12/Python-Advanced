txt = list(input())
stack = []

while txt:
    stack.append(txt.pop())

print(*stack, sep="")
