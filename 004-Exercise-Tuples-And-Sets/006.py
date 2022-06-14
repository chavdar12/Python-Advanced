def input_to_list(number_of_lines):
    my_input = []
    for _ in range(number_of_lines):
        my_input.append(input())

    return my_input


def find_the_longest_intersection(data):
    longest_intersection_length = 0
    the_longest_intersection = None
    for line in data:
        first_range, second_range = line.split("-")

        fr_left_margin, fr_right_margin = map(int, first_range.split(","))
        first_set = {*range(fr_left_margin, fr_right_margin + 1)}

        sr_left_margin, sr_right_margin = map(int, second_range.split(","))
        second_set = {*range(sr_left_margin, sr_right_margin + 1)}

        intersection = first_set.intersection(second_set)
        if len(intersection) > longest_intersection_length:
            longest_intersection_length = len(intersection)
            the_longest_intersection = intersection

    return the_longest_intersection


def print_result(result: set):
    print(f"Longest intersection is [{', '.join(map(lambda num: str(num), result))}] with length {len(result)}")


n = int(input())

lines_of_pairs_of_ranges = input_to_list(n)
longest_intersection = find_the_longest_intersection(lines_of_pairs_of_ranges)
print_result(longest_intersection)
