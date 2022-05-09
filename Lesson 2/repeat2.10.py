numbers = [int(i) for i in input().split()]

count = 0
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        count += 1

print(count)
