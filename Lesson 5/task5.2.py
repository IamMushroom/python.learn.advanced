# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
#
# Примечание. Элементы побочной диагонали также учитываются.

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

maximum = matrix[0][n - 1]
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j and matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)
