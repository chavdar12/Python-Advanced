def count_and_sort_occurrences_of_chars(given_text: str):
    characters_occurrences = {}

    for char in given_text:
        if char not in characters_occurrences:
            characters_occurrences[char] = 0
        characters_occurrences[char] += 1

    characters_occurrences = sorted(characters_occurrences.items(), key=lambda key: key[0])
    return characters_occurrences


def print_result():
    for character, number_of_occurrences in number_of_characters_occurrences:
        print(f'{character}: {number_of_occurrences} time/s')


txt = input()

number_of_characters_occurrences = count_and_sort_occurrences_of_chars(txt)
print_result()
