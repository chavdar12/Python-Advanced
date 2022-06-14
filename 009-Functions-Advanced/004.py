# def operate(opertor, *args):
#     if opertor == "+":
#         return sum(args)
#
#     if opertor == "-":
#         result = args[0]
#         for number in range(1, len(args)):
#             result -= args[number]
#
#         return result
#
#     if opertor == "*":
#         result = 1
#         for number in args:
#             result *= number
#
#         return result
#
#     if opertor == "/":
#         result = args[0]
#
#         for number in range(1, len(args)):
#             if not number == 0:
#                 result /= args[number]
#
#         return result
#
pass

from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x + y, args)

    if operator == "-":
        return reduce(lambda x, y: x - y, args)

    if operator == "*":
        return reduce(lambda x, y: x * y, args)

    if operator == "/":
        return reduce(lambda x, y: x / y, args)


pass

# from functools import reduce
#
#
# def operate(operator, *args):
#     return reduce(lambda x, y: eval(f"{x}{operator}{y}"), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 1, 2, 3))
print(operate("/", 100, 2, 1))
