from collections import deque


def reloading():
    if bullets:
        for _ in range(size_gun_barrel):
            if bullets:
                loaded_bullets.append(bullets.pop())
        print("Reloading!")


bullet_price = int(input())
size_gun_barrel = int(input())
bullets = deque(int(el) for el in input().split())
locks = deque(int(el) for el in input().split())
intelligence_value = int(input())

loaded_bullets = deque()
for _ in range(size_gun_barrel):
    if bullets:
        loaded_bullets.append(bullets.pop())

got_in = False
bullets_shot = 0
while bullets or loaded_bullets:
    bullet = loaded_bullets.popleft()
    bullets_shot += 1
    lock = locks[0]
    if bullet <= lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if not loaded_bullets:
        reloading()

    if not locks:
        got_in = True
        break

if got_in:
    money_spent_for_bullets = bullets_shot * bullet_price
    final_price = intelligence_value - money_spent_for_bullets
    bullets_left = len(bullets) + len(loaded_bullets)
    print(f"{bullets_left} bullets left. Earned ${final_price}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
