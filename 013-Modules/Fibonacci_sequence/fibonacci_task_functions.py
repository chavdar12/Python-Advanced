def create_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def locate_num_in_fibonacci(n, fib_sequence: list):
    if n in fib_sequence:
        index = fib_sequence.index(n)
        return f"The number - {n} is at index {index}"

    return f"The number {n} is not in the sequence"


if __name__ == '__main__':
    print("heyyyyy")
