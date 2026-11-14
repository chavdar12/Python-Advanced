from collections import deque

MAIN = {"red", "yellow", "blue"}
SECONDARY = {"orange": {"red", "yellow"}, "purple": {"red", "blue"}, "green": {"yellow", "blue"}}

parts = deque(input().split())
found = []

while parts:
    first = parts.popleft()
    last = parts.pop() if parts else ""
    for color in (first + last, last + first):
        if color in MAIN or color in SECONDARY:
            found.append(color)
            break
    else:
        for piece in (first[:-1], last[:-1]):
            if piece:
                parts.insert(len(parts) // 2, piece)

print([c for c in found if c in MAIN or SECONDARY[c] <= set(found)])
