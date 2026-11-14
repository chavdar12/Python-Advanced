countries = input().split(", ")
capitals = input().split(", ")
ordered = zip(countries, capitals)

[print(f"{countries[i]} -> {capitals[i]}") for i in range(len(countries))]
