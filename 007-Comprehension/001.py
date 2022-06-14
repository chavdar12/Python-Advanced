chars = input().split(", ")

dictionary = {char: ord(char) for char in chars}
print(dictionary)
