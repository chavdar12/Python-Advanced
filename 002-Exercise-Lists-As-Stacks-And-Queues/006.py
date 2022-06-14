parentheses = input()

brackets = {")": '(', "]": '[', "}": "{"}
stack = []
balanced = True

for char in parentheses:

    if char in brackets:

        if not stack or not stack[-1] == brackets[char]:
            print("NO")
            balanced = False
            break
        else:
            stack.pop()

    else:
        stack.append(char)

if balanced:
    print("YES")
