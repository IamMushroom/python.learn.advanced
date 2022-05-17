# Латинским квадратом порядка n называется квадратная матрица размером n×n, 
# каждая строка и каждый столбец которой содержат все числа от 1 до n. 
# Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

result = 'YES'
sample = [i + 1 for i in range(n)]

for row in matrix:
    sorted_row = row.copy()
    sorted_row.sort()
    if sorted_row != sample:
        result = 'NO'
        break

for j in range(n):
    row = []
    for i in range(n):
        row.append(matrix[i][j])
    row.sort()
    if row != sample:
        result = 'NO'
        break


print(result)
