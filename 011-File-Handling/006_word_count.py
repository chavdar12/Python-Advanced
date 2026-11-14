import re


def write_result_in_another_file(sorted_data: list, filename: str):
    with open(filename, "w") as file:
        [file.write(f"{word} - {count}\n") for word, count in sorted_data]


with open("../Files/words.txt") as words_file, open("../Files/text.txt") as text_file:
    all_words_in_a_string = words_file.read()
    words = all_words_in_a_string.split()
    text_from_the_text_file = text_file.read()
    words_their_count = {}
    for word in words:
        number_of_matches = len(re.findall(fr"\b{word}\b", text_from_the_text_file, re.IGNORECASE))
        words_their_count[word] = number_of_matches

sorted_dict = sorted(words_their_count.items(), key=lambda kvp: -kvp[1])
write_result_in_another_file(sorted_dict, "output.txt")
