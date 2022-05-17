# На вход программе подается нечетное натуральное число n.
# Напишите программу, которая создает матрицу размером n×n заполнив её символами . .
# Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.

n = int(input())
snowflake = []
filler = '.'
char = '*'

for i in range(n):
    row = []
    for j in range(n):
        row.append(filler)
    snowflake.append(row)

middle = n // 2
for i in range(n):
    for j in range(n):
        if i == j or i == middle or j == middle or i == n - 1 - j:
            snowflake[i][j] = char

for row in snowflake:
    print(*row)
