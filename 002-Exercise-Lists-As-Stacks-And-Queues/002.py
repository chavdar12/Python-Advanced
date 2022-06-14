number_of_lines = int(input())
stack = []

for _ in range(number_of_lines):
    query = input()

    if query.startswith("1"):
        element = int(query.split()[1])
        stack.append(element)

    if stack:
        if query == "2":
            if stack:
                stack.pop()

        elif query == "3":
            print(max(stack))

        elif query == "4":
            print(min(stack))

if stack:
    print(*[stack.pop() for _ in range(len(stack))], sep=", ")
