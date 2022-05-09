numbers = []

for i in input().split():
    if i not in numbers:
        numbers.append(i)

print(len(numbers))
