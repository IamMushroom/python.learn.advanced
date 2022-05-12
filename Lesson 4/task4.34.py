# На вход программе подаются два натуральных числа n и m.
# Напишите программу, которая создает матрицу размером n×m
# заполнив её в соответствии с образцом.

n, m = [int(i) for i in input().split()]
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = i + j + 1
        if elem > m:
            elem = elem - m * (elem // m)
        if elem == 0:
            elem = m
        row.append(str(elem).ljust(2))
    matrix.append(row)

for row in matrix:
    print(*row)
