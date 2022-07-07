# Даны два натуральных числа m и n. Напишите программу, которая сокращает дробь m/n и выводит ее.

from fractions import Fraction


def solution() -> None:
    m, n = int(input()), int(input())
    print(Fraction(m, n))


if __name__ == '__main__':
    solution()
