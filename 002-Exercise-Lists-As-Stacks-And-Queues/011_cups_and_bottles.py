from collections import deque

cups = deque(int(el) for el in input().split())
bottles = deque(int(el) for el in input().split())

wasted_water = 0
while bottles and cups:

    if cups[0] > bottles[-1]:
        cups[0] -= bottles.pop()

    elif cups[0] == bottles[-1]:
        cups.popleft()
        bottles.pop()

    elif cups[0] < bottles[-1]:
        wasted_water += bottles.pop() - cups.popleft()

if bottles:
    print("Bottles:", end=" ")
    print(*bottles)

elif cups:
    print("Cups: ", end="")
    print(*cups)

print(f"Wasted litters of water: {wasted_water}")
