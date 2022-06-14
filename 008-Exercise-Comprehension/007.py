nums = [[element for element in el.split() if not element == ' '] for el in input().split("|")]
nums.reverse()
print(*[each for row in nums for each in row])
