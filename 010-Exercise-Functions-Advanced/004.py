def separate_positive_from_negative_nums(numbers):
    positive = []
    negative = []

    for num in numbers:
        if num >= 0:
            positive.append(num)
            continue

        negative.append(num)

    return positive, negative


def print_results(negative_list, positive_list):
    negative_list_sum = sum(negative_list)
    positive_list_sum = sum(positive_list)
    print(negative_list_sum, positive_list_sum, sep="\n")

    stronger, weaker = "positives", "negatives"
    if abs(negative_list_sum) > positive_list_sum:
        stronger, weaker = "negatives", "positives"

    print(f"The {stronger} are stronger than the {weaker}")


numbers = [int(num) for num in input().split()]
positive_numbers, negative_numbers = separate_positive_from_negative_nums(numbers)
print_results(negative_numbers, positive_numbers)
