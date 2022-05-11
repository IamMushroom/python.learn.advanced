# Напишите программу, которая поворачивает квадратную матрицу чисел
# на 90∘ по часовой стрелке.

from math import ceil
n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

result_matrix = []
for j in range(n):
    row = []
    for i in range(n - 1, -1, -1):
        row.append(matrix[i][j])
    result_matrix.append(row)

for row in result_matrix:
    print(*row)
