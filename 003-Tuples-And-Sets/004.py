def input_to_list(number_of_lines):
    my_input = []
    for _ in range(number_of_lines):
        my_input.append(input())

    return my_input


def cars_remaining_in_parking_lot(cars):
    cars_in_parking_lot = set()
    for car in cars:
        direction, license_plate = car.split(", ")
        if direction == "IN":
            cars_in_parking_lot.add(license_plate)
        else:
            cars_in_parking_lot.remove(license_plate)

    return cars_in_parking_lot


def print_result(remaining):
    if remaining:
        print(*remaining, sep="\n")
    else:
        print("Parking Lot is Empty")


n = int(input())

cars_movements = input_to_list(n)
remaining_cars = cars_remaining_in_parking_lot(cars_movements)
print_result(remaining_cars)
