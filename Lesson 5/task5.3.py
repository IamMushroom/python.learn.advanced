# Напишите программу, которая транспонирует квадратную матрицу.

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row)
