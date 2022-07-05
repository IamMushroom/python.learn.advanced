# Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы неравенств

from random import uniform


def solution() -> None:
    """
    Решение
    """
    n = 10 ** 6
    k = 0
    S0 = 16

    for _ in range(n):
        x = uniform(-2, 2)
        y = uniform(-2, 2)
        if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
            k += 1
    s = (k / n) * S0
    print(s)


if __name__ == '__main__':
    solution()
