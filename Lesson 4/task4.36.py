# На вход программе подаются два натуральных числа n и m.
# Напишите программу, которая создает матрицу размером n×m
# заполнив её "диагоналями" в соответствии с образцом.

n, m = [int(i) for i in input().split()]
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = ''
        row.append('')
    matrix.append(row)

nm = 0
for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                matrix[i][j] = str(nm).ljust(2)

for row in matrix:
    print(*row)
