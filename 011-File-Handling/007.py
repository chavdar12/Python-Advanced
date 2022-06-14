import re


def write_result_in_another_file(sorted_data: list, filename: str):
    with open(filename, "w") as file:
        for word, count in sorted_data:
            file.write(f"{word} - {count}\n")


def return_file_content_as_words(file_path: str) -> list:
    with open(file_path) as file:
        all_words_in_a_string = file.read()
        words = all_words_in_a_string.split()

    return words


def return_lowercase_text(file_path: str) -> str:
    with open(file_path) as file:
        txt = file.read().lower()

    return txt


def count_matches(words: list, txt: str) -> dict:
    word_count = {}
    for word in words:
        matches = len(re.findall(fr"\b{word}\b", txt))
        word_count[word] = matches

    return word_count


target_words = return_file_content_as_words("../Files/words.txt")
target_text = return_lowercase_text("../Files/text.txt")
words_and_their_count = count_matches(target_words, target_text)
words_and_their_count = sorted(words_and_their_count.items(), key=lambda kvp: -kvp[1])
write_result_in_another_file(words_and_their_count, "output.txt")
