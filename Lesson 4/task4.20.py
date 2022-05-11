# Напишите программу, которая находит индексы (строку и столбец)
# первого вхождения максимального элемента.

# Заполняем матрицу
n, m = int(input()), int(input())
matrix = []
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

# Находим максимум
maximum = matrix[0][0]
max_i, max_j = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            max_i = i
            max_j = j

print(max_i, max_j)
