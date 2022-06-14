from collections import deque

my_queue = deque()

command = input()
while not command == "End":

    if command == "Paid":
        while my_queue:
            print(my_queue.popleft())

        command = input()
        continue

    my_queue.append(command)
    command = input()

print(f"{len(my_queue)} people remaining.")
