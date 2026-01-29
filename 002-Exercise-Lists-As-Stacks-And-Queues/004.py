clothes = list(map(int, input().split()))
single_rack_capacity = int(input())
rack_space_occupied = 0
rack_counter = 1

for _ in range(len(clothes)):

    current_item_clothing = clothes.pop()

    if rack_space_occupied + current_item_clothing > single_rack_capacity:
        rack_counter += 1
        rack_space_occupied = 0

    rack_space_occupied += current_item_clothing

print(rack_counter)
