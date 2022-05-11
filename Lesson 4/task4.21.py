# Напишите программу, которая меняет местами столбцы в матрице.

# Заполняем матрицу
n, m = int(input()), int(input())
matrix = []
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

change = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][change[0]], matrix[i][change[1]
                                    ] = matrix[i][change[1]], matrix[i][change[0]]

for row in matrix:
    print(*row)
