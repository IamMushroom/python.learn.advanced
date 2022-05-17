# На вход программе подаются два натуральных числа n и m.
# Напишите программу, которая создает матрицу размером n×m
# заполнив её "спиралью" в соответствии с образцом.

n, m = [int(i) for i in input().split()]
matrix = []

if n == 1 or m == 1:
    elem = 1
    for i in range(n):
        row = []
        for j in range(m):
            row.append(str(elem).ljust(2))
            elem += 1
        matrix.append(row)
else:
    for i in range(n):
        row = []
        for j in range(m):
            elem = ''
            row.append('')
        matrix.append(row)

    current_direction = 0
    i, j = 0, 0
    for q in range(n * m):
        if matrix[i][j] == '':
            matrix[i][j] = str(q + 1).ljust(2)
        if current_direction == 0:
            j += 1
            if j == m - 1 or matrix[i][j + 1] != '':
                current_direction = 1
        elif current_direction == 1:
            i += 1
            if i == n - 1 or matrix[i + 1][j] != '':
                current_direction = 2
        elif current_direction == 2:
            j -= 1
            if j == 0 or matrix[i][j - 1] != '':
                current_direction = 3
        elif current_direction == 3:
            i -= 1
            if i == 0 or matrix[i - 1][j] != '':
                current_direction = 0
        
for row in matrix:
    print(*row)

