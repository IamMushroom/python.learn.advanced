# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения

from fractions import Fraction
from math import factorial


def get_sum(__n: int) -> Fraction:
    result = Fraction(0)
    for i in range(1, __n + 1):
        result += Fraction(1, factorial(i))
    return result


def solution() -> None:
    print(get_sum(int(input())))


if __name__ == '__main__':
    solution()
