def age_assignment(*args, **kwargs):
    name_age = {}
    for name in args:
        first_letter = name[0]
        name_age[name] = kwargs[name[0]]

    return name_age


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
