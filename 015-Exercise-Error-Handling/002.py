class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


email = input()

if '@' not in email:
    raise MustContainAtSymbolError("Email must contain @")

elif '@' in email:
    name = []
    for el in email:
        if el == "@":
            break
        name.append(el)
    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

valid_domains = [".com", ".bg", ".org", ".net"]
