def get_lines(file_path: str) -> list:
    with open(file_path) as file:
        text = [line[:-1] for line in file.readlines()]

    return text


def get_punctuation_count(text: str) -> int:
    punctuation_marks = 0
    for char in text:
        if not char.isalnum() and not char == " ":
            punctuation_marks += 1

    return punctuation_marks


def get_letters_counts(text: str) -> int:
    letters = 0
    for char in text:
        if char.isalnum():
            letters += 1

    return letters


def get_characters_count_and_format_output(result):
    formatted = []
    for i in range(len(result)):
        punctuation_marks_count = get_punctuation_count(result[i])
        letters_count = get_letters_counts(result[i])
        formatted.append(f"Line {i + 1}: {lines[i]} ({letters_count})({punctuation_marks_count})\n")

    return formatted


def write_result_in_file(result, file_path: str):
    with open(file_path, "w") as file:
        file.writelines(result)


lines = get_lines("../Files/line_numbers.txt")
lines = format_output(lines)
write_result_in_file(lines, "line_numbers_output.txt")
