# Перемножение матриц

a = []
b = []
n, m = 2, 2

for i in range(n):
    a.append([int(q) for q in input().split()])

for i in range(m):
    b.append([int(q) for q in input().split()])

c = []
for i in range(n):
    row = []
    for j in range(n):
        sum = 0
        for k in range(m):
            sum += a[i][k] * b[k][j]
        row.append(str(sum).ljust(2))
    c.append(row)

for row in c:
    print(*row)
