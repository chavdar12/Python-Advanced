from collections import deque

kids = deque(input().split())
hot_potato = int(input())

while len(kids) > 1:
    kids.rotate(-hot_potato)
    print(f"Removed {kids.pop()}")
    # for _ in range(hot_potato - 1):
    #     kids.popleft()

print(f"Last is {kids[0]}")
