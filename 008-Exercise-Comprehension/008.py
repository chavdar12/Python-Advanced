names = input().split(", ")
dicky = {name: {"Weapon": [], "Cost": 0} for name in names}

info = input()
while not info == "End":
    name, weapon, cost = info.split("-")

    if weapon not in dicky[name]["Weapon"]:
        dicky[name]["Weapon"].append(weapon)
        dicky[name]["Cost"] += int(cost)

    info = input()

for name, items in dicky.items():
    print(f"{name} -> Items: {len(items['Weapon'])}, Cost: {items['Cost']}")
