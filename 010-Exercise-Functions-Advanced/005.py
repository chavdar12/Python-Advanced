def get_sum_of_even_or_odd_nums_multiplied_by_overall_count(odd_or_even: str, numbers: list):
    count = len(numbers)
    if odd_or_even == "Odd":
        numbers = [number for number in numbers if number % 2 == 1]
    elif odd_or_even == "Even":
        numbers = filter(lambda x: not x % 2, numbers)
    return sum(numbers) * count


command = input()
numbers = [int(el) for el in input().split()]
print(get_sum_of_even_or_odd_nums_multiplied_by_overall_count(command, numbers))
