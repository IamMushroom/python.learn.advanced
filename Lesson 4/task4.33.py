# На вход программе подается натуральное число n.
# Напишите программу, которая создает матрицу размером n×n
# заполнив её в соответствии с образцом.

n = int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        if (i > j and i < n - 1 - j) or (i < j and i > n - 1 - j):
            elem = '0'
        else:
            elem = '1'
        row.append(elem.ljust(2))
    matrix.append(row)

for row in matrix:
    print(*row)
