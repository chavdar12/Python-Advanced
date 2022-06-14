class MustBeInteger(Exception):
    pass


try:
    text = input()
    times = int(input())

except ValueError:
    print("Variable times must be an integer")

else:
    print(text * times)
