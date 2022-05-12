# Напишите программу для создания матрицы размером n×m,
# заполнив её символами . и * в шахматном порядке.
# В левом верхнем углу должна стоять точка.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.

fill_primary = '.'
fill_secondary = '*'

n, m = [int(i) for i in input().split()]
board = []

for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2 == 0:
            row.append(fill_primary)
        else:
            row.append(fill_secondary)
    board.append(row)

for row in board:
    print(*row)
