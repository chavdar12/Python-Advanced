# from itertools import combinations
#
# names = list(combinations(input().split(", "), int(input())))
#
# for name in names:
#     print(*name, sep=", ")
##########################3 only 50%
names = input().split(", ")
chairs = int(input())


def combination(names, chairs, current_names=[]):
    if len(current_names) == chairs:
        print(*current_names, sep=", ")
        return

    for i in range(len(names)):
        current_names.append(names[i])
        combination(names[i + 1:], chairs, current_names)
        current_names.pop()


combination(names, chairs)
