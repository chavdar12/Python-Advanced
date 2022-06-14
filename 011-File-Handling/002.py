try:
    with open("../Files/numbers.txt", "r") as file:
        sum_of_nums = 0
        for el in file:
            sum_of_nums += int(el)

        print(sum_of_nums)

except FileNotFoundError:

    print("file not found")
