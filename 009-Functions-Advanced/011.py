def fml(numbers, current_result=0, current_expression=""):
    if not numbers:
        print(f"{current_expression}={current_result}")
        return
    fml(numbers[1:], current_result + numbers[0], f"{current_expression}+{numbers[0]}")
    fml(numbers[1:], current_result - numbers[0], f"{current_expression}-{numbers[0]}")


nums = [int(el) for el in input().split(", ")]

fml(nums)
