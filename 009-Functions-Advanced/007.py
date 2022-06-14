def perm(text: list, idx=0):
    if idx == len(text):
        print("".join(text))
        return

    for i in range(idx, len(text)):
        text[idx], text[i] = text[i], text[idx]
        perm(text, idx + 1)
        text[idx], text[i] = text[i], text[idx]


perm(list(input()))
