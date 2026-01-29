def recursive_power(num, power):
    if power == 1:
        return num
    return num * recursive_power(num, power - 1)


from math import pow

print(int(pow(2, 10)))
print(recursive_power(2, 10))
