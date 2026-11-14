def permutations(chars: list):
    if len(chars) == 1:
        return chars

    combos = []
    for char in chars:
        rest = [x for x in chars if not x == char]
        sub_lists = permutations(rest)

        for each in sub_lists:
            combos.append(char + each)

    return combos


print(*permutations(list(input())), sep="\n")
