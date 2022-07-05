# Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа π

from random import uniform


def solution() -> None:
    """
    Решение
    """
    n = 10 ** 6
    k = 0
    S0 = 4

    for _ in range(n):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            k +=1
    s = (k / n) * S0
    print(s)


if __name__ == '__main__':
    solution()
