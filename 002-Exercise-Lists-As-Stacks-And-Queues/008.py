from collections import deque
from datetime import datetime, timedelta


def set_robot_to_work():
    current_robo = available_robots.popleft()
    current_robo["Available_at"] = time + timedelta(seconds=current_robo["Time"])
    print(f"{current_robo['Name']} - {current_product} [{time.time()}]")


robots_info = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")

robots = []
available_robots = deque()
products = deque()

for each_robot in robots_info:  # fills robots and available_robots
    name, processing_time = each_robot.split("-")
    robot = {
        "Name": name,
        "Time": int(processing_time),
        "Available_at": time
    }
    robots.append(robot)
    available_robots.append(robot)

product = input()
while not product == "End":  # fills products
    products.append(product)
    product = input()

time += timedelta(seconds=1)

while products:  # gives products to robots
    current_product = products.popleft()

    if available_robots:
        set_robot_to_work()

    else:
        for each_robo in robots:
            if each_robo["Available_at"] <= time:
                available_robots.append(each_robo)

        if available_robots:
            set_robot_to_work()

        else:
            products.append(current_product)

    time += timedelta(seconds=1)
