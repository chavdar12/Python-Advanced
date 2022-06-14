def input_to_list(number_of_lines):
    my_input = []
    for _ in range(number_of_lines):
        my_input.append(input())

    return my_input


def input_to_unknown_lines():
    command = input()
    guests = []
    while not command == "END":
        guests.append(command)
        command = input()

    return guests


def get_no_show_guests(reservations, guests):
    no_shows = set(reservations).difference(guests)

    return no_shows


def order_no_shows(guest_list):
    vips = []
    regulars = []

    for guest in guest_list:
        if guest[0].isdigit():
            vips.append(guest)
        else:
            regulars.append(guest)

    vips_sorted = sorted(vips)
    regulars_sorted = sorted(regulars)

    return vips_sorted + regulars_sorted


def print_result(final_list):
    print(len(final_list))
    print(*final_list, sep="\n")


n = int(input())

reservations = input_to_list(n)
guests = input_to_unknown_lines()
no_show_guests = get_no_show_guests(reservations, guests)
ordered_no_shows = order_no_shows(no_show_guests)
print_result(ordered_no_shows)
