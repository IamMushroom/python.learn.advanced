# Уравнение параболы имеет вид y = ax^2 + bx + c , где a != 0. Напишите программу, которая по введенным значениям a, b, c определяет и выводит вершину параболы.

def solve(a, b, c):
    x = -1 * (b / (2 * a))
    y = ((4 * a * c) - b ** 2) / (4 * a)
    return x, y


a, b, c = int(input()), int(input()), int(input())
print(solve(a, b, c))
