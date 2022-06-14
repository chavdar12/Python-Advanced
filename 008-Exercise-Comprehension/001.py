words = input().split()

print('\n'.join([word for word in words if len(word) % 2 == 0]))
