some_text = input().split(", ")

print(', '.join([f"{item} -> {len(item)}" for item in some_text]))
