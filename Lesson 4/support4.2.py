# Возведение матрицы в степень

a = []
b = []
n, m, power = 2, 2, 25

for i in range(n):
    a.append([int(q) for q in input().split()])

b = a

for _ in range(power - 1):
    c = []
    for i in range(n):
        row = []
        for j in range(n):
            sum = 0
            for k in range(m):
                sum += int(a[i][k]) * b[k][j]
            row.append(str(sum).ljust(2))
        c.append(row)
    a = c

for row in c:
    print(*row)
