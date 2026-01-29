class ValueCannotBeNegative(Exception):
    pass


class ValueTooSmallError(ValueCannotBeNegative):
    for i in range(5):
        num = int(input())
        if num < 0:
            raise ValueCannotBeNegative
