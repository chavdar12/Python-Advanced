class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    if int(input()) < 0:
        raise ValueCannotBeNegative
