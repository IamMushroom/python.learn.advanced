# Напишите программу, которая сначала считывает
# элементы матрицы один за другим,
# затем выводит их в виде матрицы.

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = []
    for __ in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    print(*matrix[i])
