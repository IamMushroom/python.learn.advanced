# Напишите программу, которая выводит максимальный элемент
# в заштрихованной области квадратной матрицы.
# Элементы диагоналей также учитываются.

n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)


maximum = matrix[0][0]
for i in range(n):
    for j in range(n):
        if (i >= j and i <= (n - 1 - j)) or (i <= j and i >= (n - 1 - j)):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)
