from Fibonacci_sequence.fibonacci_task_functions import *

command = input()

while not command == "Stop":
    if "Create" in command:
        number = int(command.split()[2])
        fib_sequence = create_fibonacci_sequence(number)
        print(*fib_sequence)

    if "Locate" in command:
        number = int(command.split()[1])
        print(locate_num_in_fibonacci(number, fib_sequence))

    command = input()