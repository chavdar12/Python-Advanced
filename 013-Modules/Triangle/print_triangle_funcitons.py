def print_upper_part(n):
    for row in range(1, n + 1):
        for col in range(row):
            print("*", end="")
        print()


def print_lower_part(n):
    for row in range(n - 1, 0, -1):
        for col in range(row):
            print("*", end="")
        print()


def print_whole(n):
    print_upper_part(n)
    print_lower_part(n)
