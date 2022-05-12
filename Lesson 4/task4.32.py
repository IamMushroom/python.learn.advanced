# На вход программе подается натуральное число n.
# Напишите программу, которая создает матрицу размером n×n
# заполнив её в соответствии с образцом.

n = int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        if i == j or i == n - 1 - j:
            elem = '1'
        else:
            elem = '0'
        row.append(elem.ljust(2))
    matrix.append(row)

for row in matrix:
    print(*row)
