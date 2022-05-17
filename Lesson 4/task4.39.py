# Напишите программу, которая перемножает две матрицы.

a = []
b = []

n, m = [int(i) for i in input().split()]
for _ in range(n):
    a.append([int(q) for q in input().split()])

input()

m, k = [int(i) for i in input().split()]
for _ in range(m):
    b.append([int(q) for q in input().split()])

c = []
for i in range(n):
    row = []
    for j in range(k):
        sum = 0
        for q in range(m):
            sum += a[i][q] * b[q][j]
        row.append(str(sum).ljust(2))
    c.append(row)

for row in c:
    print(*row)
