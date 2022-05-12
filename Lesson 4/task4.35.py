# На вход программе подаются два натуральных числа n и m. 
# Напишите программу, которая создает матрицу размером n×m 
# заполнив её "змейкой" в соответствии с образцом.

n, m = [int(i) for i in input().split()]
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = i * m + j + 1
        row.append(str(elem).ljust(3))
    if i % 2 == 1:
        row.reverse()
    matrix.append(row)

for row in matrix:
    print(*row, sep='')
