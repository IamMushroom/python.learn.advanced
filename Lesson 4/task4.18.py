# Квадратная матрица разбивается на четыре четверти,
# ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
# Напишите программу, которая вычисляет сумму элементов:
# верхней четверти; правой четверти; нижней четверти; левой четверти.
# Элементы диагоналей не учитываются.

n = int(input())
matrix = []

for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

upper_quarter, right_quarter, lower_quarter, left_quarter = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i > j:
            if i < n - 1 - j:
                left_quarter += matrix[i][j]
            elif i > n - 1 - j:
                lower_quarter += matrix[i][j]
        elif i < j:
            if i < n - 1 - j:
                upper_quarter += matrix[i][j]
            elif i > n - 1 - j:
                right_quarter += matrix[i][j]

print(f'Верхняя четверть: {upper_quarter}')
print(f'Правая четверть: {right_quarter}')
print(f'Нижняя четверть: {lower_quarter}')
print(f'Левая четверть: {left_quarter}')
