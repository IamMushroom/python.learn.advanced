n = int(input())
numbers = [int(input()) for i in range(n)]
mult = int(input())

result = 'НЕТ'
for i in range(n - 1):
    for j in range(i + 1, n):
        if numbers[i] * numbers[j] == mult:
            result = 'ДА'
            break

print(result)
