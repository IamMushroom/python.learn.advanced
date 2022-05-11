# Напишите программу, которая выводит максимальный элемент
# в заштрихованной области квадратной матрицы.
# Элементы главной диагонали также учитываются.

n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

maximum = matrix[0][0]
for i in range(n):
    for j in range(i + 1):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)
