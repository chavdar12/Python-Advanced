from itertools import permutations

glist = list(permutations(list(input())))
for item in glist:
    print(*item, sep="")
