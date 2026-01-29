from collections import deque
from datetime import datetime, timedelta

robots_info = input().split(";")

time = datetime.strptime(input(), "%H:%M:%S")

robots = []  # list of robots with their characteristics in a dictionary
available_robots = deque()
for el in robots_info:
    robot_name, processing_time = el.split("-")

    robot = {
        "Robot_name": robot_name,
        "Processing_time": int(processing_time),
        "Available_at": time
    }

    robots.append(robot)
    available_robots.append(robot)

products = deque()  # list of products
product = input()
while not product == "End":
    products.append(product)
    product = input()

time += timedelta(seconds=1)
while products:
    current_product = products.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['Available_at'] = time + timedelta(seconds=current_robot['Processing_time'])
        print(f"{current_robot['Robot_name']} - {current_product} [{time.time()}]")

    else:
        for robby in robots:
            if time >= robby['Available_at']:
                available_robots.append(robby)

        if not available_robots:
            products.append(current_product)

        else:
            current_robot = available_robots.popleft()
            current_robot['Available_at'] = time + timedelta(seconds=current_robot['Processing_time'])
            print(f"{current_robot['Robot_name']} - {current_product} [{time.time()}]")

    time += timedelta(seconds=1)
