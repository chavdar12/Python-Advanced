from collections import deque

number_petrol_pumps = int(input())

pumps = deque([])
for _ in range(number_petrol_pumps):
    petrol, distance_to_next_pump = [int(el) for el in input().split()]
    petrol_left = petrol - distance_to_next_pump
    pumps.append(petrol_left)

counter = 0
while True:
    distance = 0

    for position in range(len(pumps)):
        distance += pumps[position]

        if distance < 0:
            counter += 1
            pumps.rotate(-1)
            break

    if distance >= 0:
        break

print(counter)
