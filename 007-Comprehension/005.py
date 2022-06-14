start_int = int(input())
end_int = int(input())

print([num for num in range(start_int, end_int + 1) if [1 for divisor in range(2, 11) if num % divisor == 0]])
