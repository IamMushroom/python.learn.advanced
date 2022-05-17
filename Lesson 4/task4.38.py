# Напишите программу для вычисления суммы двух матриц.

n, m = [int(i) for i in input().split()]

a, b = [], []
for _ in range(n):
    a.append([int(i) for i in input().split()])
input()
for _ in range(n):
    b.append([int(i) for i in input().split()])

c = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(a[i][j] + b[i][j])
    c.append(row)

for row in c:
    print(*row)
