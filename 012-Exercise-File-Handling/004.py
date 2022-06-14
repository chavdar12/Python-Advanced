import os.path


def create_file(file_name):
    file = open(file_name, "w")
    file.close()


def add_content_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(f"{content}\n")


def replace_content(file_name, old_content, new_content):
    if file_exists(file_name):
        with open(file_name) as file:
            text = file.read()

        text = text.replace(old_content, new_content)

        with open(file_name, "w") as file:
            file.write(text)


def delete_file(filename):
    if file_exists(filename):
        os.remove(filename)


def file_exists(filename):
    if os.path.exists(filename):
        return True

    print("An error occurred")


def main():
    command = input()
    while not command == "End":
        action, file_name = command.split("-")[0], command.split("-")[1]
        if action == "Create":
            create_file(file_name)

        elif action == "Add":
            content = command.split("-")[2]
            add_content_to_file(file_name, content)

        elif action == "Replace":
            old_string = command.split("-")[2]
            new_string = command.split("-")[3]
            replace_content(file_name, old_string, new_string)

        elif action == "Delete":
            delete_file(file_name)

        command = input()


main()
