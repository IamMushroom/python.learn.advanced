# Дана квадратная матрица чисел.
# Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

from math import floor

n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

for i in range(floor(n / 2)):
    matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

for row in matrix:
    print(*row)
