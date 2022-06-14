from math import log


def get_result(n, base):
    result = log(n)
    if not base_of_logarithm == "natural":
        result = log(n, int(base_of_logarithm))

    return result


n = int(input())
base_of_logarithm = input()

result = get_result(n, base_of_logarithm)

print(f"{result:.2f}")
