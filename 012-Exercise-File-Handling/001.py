def get_each_line(file_path: str) -> list:
    with open(file_path) as file:
        text = [line[:-1] for line in file.readlines()]

    return text


def get_each_second_line(lines: list) -> list:
    even_lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]
    return even_lines


def replace_characters(text: list, to_be_replaced: list, replacer: str) -> list:
    reformatted_text = []
    for line in text:
        for char in line:
            if char in to_be_replaced:
                line = line.replace(char, replacer)
        reformatted_text.append(line)
    return reformatted_text


def print_result(result: list):
    for line in result:
        words = line.split()
        print(*list(reversed(words)))


SPECIAL_CHARACTERS = ["-", ",", ".", "!", "?"]

lines = get_each_line("../Files/even_lines.txt")
even_lines = get_each_second_line(lines)
even_lines_without_special_characters = replace_characters(even_lines, SPECIAL_CHARACTERS, "@")
print_result(even_lines_without_special_characters)
