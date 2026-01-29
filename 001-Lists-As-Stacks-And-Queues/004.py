from collections import deque

water = int(input())

people_in_line = deque()
while True:
    name = input()
    if name == "Start":
        break
    people_in_line.append(name)

while True:
    command = input()
    if command == "End":
        print(f"{water} liters left")
        break

    if command.isdigit():
        if int(command) > water:
            print(f"{people_in_line.popleft()} must wait")
        else:
            water -= int(command)
            print(f"{people_in_line.popleft()} got water")

    elif command.startswith("refill"):
        water += int(command.split(" ")[1])
