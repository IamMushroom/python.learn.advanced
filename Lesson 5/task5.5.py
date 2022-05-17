# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

result = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)
