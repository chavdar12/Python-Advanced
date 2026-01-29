from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
crash = False
cars_successfully_crossed = 0
car_or_command = input()
while not car_or_command == "END":
    if not car_or_command == "green":
        cars.append(car_or_command)

    else:
        green = green_light_duration
        free_window = free_window_duration

        while cars and green > 0:
            car_entering_the_crossroads = cars.popleft()
            car_entering_the_crossroads = {"Name": car_entering_the_crossroads,
                                           'Length': len(car_entering_the_crossroads)}
            green -= car_entering_the_crossroads['Length']

            if green >= 0:
                cars_successfully_crossed += 1

            else:
                car_length_left = abs(green)
                if car_length_left <= free_window:
                    cars_successfully_crossed += 1
                else:
                    car_length_left -= free_window
                    hit_letter = car_entering_the_crossroads['Name'][-car_length_left]
                    print(f"A crash happened!\n{car_entering_the_crossroads['Name']} was hit at {hit_letter}.")
                    crash = True
    if crash:
        break

    car_or_command = input()

if not crash:
    print("Everyone is safe.\n"
          f"{cars_successfully_crossed} total cars passed the crossroads.")
