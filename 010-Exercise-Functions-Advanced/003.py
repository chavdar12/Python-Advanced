def print_result(min, max, tots):
    print(f"The minimum number is {min}",
          f"The maximum number is {max}",
          f"The sum number is: {tots}", sep="\n")


numbers = [int(num) for num in input().split()]
minimal = min(numbers)
maximal = max(numbers)
total_sum = sum(numbers)

print_result(minimal, maximal, total_sum)
