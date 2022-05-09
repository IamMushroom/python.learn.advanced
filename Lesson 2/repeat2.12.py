numbers = [int(i) for i in input().split()]

last_number = numbers[len(numbers) - 1]
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]
numbers[0] = last_number

print(*numbers)
