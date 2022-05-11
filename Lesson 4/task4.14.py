# Следом квадратной матрицы называется сумма элементов главной диагонали.
# Напишите программу, которая выводит след заданной квадратной матрицы.

n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

summ = 0
for i in range(n):
    summ += matrix[i][i]

print(summ)
