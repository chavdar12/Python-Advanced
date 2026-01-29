try:
    open("../Files/text.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")
