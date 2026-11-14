from collections import deque

PRESENTS = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))
crafted = {}

while materials and magic:
    material, level = materials[-1], magic[0]
    if material == 0 or level == 0:
        if material == 0:
            materials.pop()
        if level == 0:
            magic.popleft()
        continue

    product = material * level
    if product in PRESENTS:
        materials.pop()
        magic.popleft()
        crafted[PRESENTS[product]] = crafted.get(PRESENTS[product], 0) + 1
    elif product < 0:
        materials.pop()
        magic.popleft()
        materials.append(material + level)
    else:
        magic.popleft()
        materials[-1] += 15

done = {"Doll", "Wooden train"} <= crafted.keys() or {"Teddy bear", "Bicycle"} <= crafted.keys()
print("The presents are crafted! Merry Christmas!" if done else "No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")
for name in sorted(crafted):
    print(f"{name}: {crafted[name]}")
