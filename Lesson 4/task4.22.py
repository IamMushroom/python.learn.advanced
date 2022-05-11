# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

result = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break

print(result)
