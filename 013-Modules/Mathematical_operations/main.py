from Mathematical_operations.mapper import mapper

num1, operator, num2 = input().split()
num1 = float(num1)
num2 = float(num2)

print(f"{mapper.get(operator)(num1, num2):.2f}" if mapper.get(operator) else f"no such operator")
