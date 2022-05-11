# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

n, m = int(input()), int(input())

mult = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(i * j)
    mult.append(row)

for row in mult:
    for num in row:
        print(str(num).ljust(3), end='')
    print()
