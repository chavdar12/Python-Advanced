class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = (".com", ".bg", ".org", ".net")

email = input()
while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@", 1)
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if "." + domain.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")

    print("Email is valid")
    email = input()
