# Напишите программу, которая выводит количество элементов квадратной матрицы
# в каждой строке, больших среднего арифметического элементов данной строки.

n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

for row in matrix:
    avg = sum(row) / len(row)
    count = 0
    for num in row:
        if num > avg:
            count += 1
    print(count)
