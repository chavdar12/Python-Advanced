from collections import deque

effects = deque(int(x) for x in input().split(", "))
powers = [int(x) for x in input().split(", ")]
fireworks = {"Palm": 0, "Willow": 0, "Crossette": 0}

while effects and powers and not all(count >= 3 for count in fireworks.values()):
    if effects[0] <= 0:
        effects.popleft()
        continue
    if powers[-1] <= 0:
        powers.pop()
        continue

    total = effects[0] + powers[-1]
    kind = "Crossette" if total % 15 == 0 else "Palm" if total % 3 == 0 else "Willow" if total % 5 == 0 else None
    if kind:
        fireworks[kind] += 1
        effects.popleft()
        powers.pop()
    else:
        effects.append(effects.popleft() - 1)

if all(count >= 3 for count in fireworks.values()):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if powers:
    print(f"Explosive Power left: {', '.join(map(str, powers))}")
for kind, count in fireworks.items():
    print(f"{kind} Fireworks: {count}")
