def input_as_dict_and_integer_num_searches():
    names_phone_numbers = {}
    info = input()
    while not info.isdigit():
        name, phone_number = info.split("-")
        names_phone_numbers[name] = phone_number
        info = input()

    return names_phone_numbers, int(info)


def searches_in_phonebook_and_prints_result(phone_book: dict, count: int):
    for _ in range(count):
        name = input()
        if name in phone_book:
            print(f"{name} -> {phone_book[name]}")
        else:
            print(f"Contact {name} does not exist.")


phonebook, number_of_searches = input_as_dict_and_integer_num_searches()
searches_in_phonebook_and_prints_result(phonebook, number_of_searches)
