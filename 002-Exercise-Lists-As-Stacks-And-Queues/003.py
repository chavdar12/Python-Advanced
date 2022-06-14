from collections import deque

food_available = int(input())
list_of_orders = deque(map(int, input().split()))

print(max(list_of_orders))

while True:

    if food_available < list_of_orders[0]:
        print(f"Orders left: {' '.join(map(str, list_of_orders))}")
        break

    food_available -= list_of_orders.popleft()

    if not list_of_orders:
        print('Orders complete')
        break
