# Дана квадратная матрица чисел.
#
# Напишите программу, которая меняет местами элементы,
# стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце
# (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).

n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]

for row in matrix:
    print(*row)
