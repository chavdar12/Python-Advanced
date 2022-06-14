import os


def get_extension(file):
    extension = ""
    for i in range(len(file), -1, -1):
        extension = file[i - 1] + extension
        if file[i - 1] == ".":
            break

    return extension


def file_extensions_and_associated_files(files):
    extension_files = {}
    for file in files:
        extension = get_extension(file)
        if extension not in extension_files:
            extension_files[extension] = []
        extension_files[extension].append(file)

    return extension_files


def format_output(files):
    with open(os.path.expanduser("~/Desktop/report.txt"), "w") as file:
        for extension, files_names in files:
            file.write(extension + "\n")
            files_names = sorted(files_names)
            for file_name in files_names:
                file.write(f"---{file_name}\n")


_, _, files = next(os.walk(input()))

extensions_files = file_extensions_and_associated_files(files)
ordered_extension_files = sorted(extensions_files.items(), key=lambda kvp: kvp[0])
format_output(ordered_extension_files)
