txt = input()

print(''.join([char for char in txt if char.lower() not in ["a", "o", "u", "e", "i"]]))
