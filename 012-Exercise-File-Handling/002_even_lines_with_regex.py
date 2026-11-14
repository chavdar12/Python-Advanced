import re

file = open("../Files/even_lines.txt")
text = file.readlines()
file.close()

for idx, line in enumerate(text):

    if idx % 2 == 0:
        line = re.sub("[-,.!?]", "@", line.strip("\n"))
        print(*list(reversed(line.split())))
