# Напишите программу, которая считывает элементы матрицы
# один за другим, выводит их в виде матрицы,
# выводит пустую строку, и снова ту же матрицу,
# но уже поменяв местами строки со столбцами:
# первая строка выводится как первый столбец, и так далее.

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = []
    for __ in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    print(*matrix[i])

print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()
