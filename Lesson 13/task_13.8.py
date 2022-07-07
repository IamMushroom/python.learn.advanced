# Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и частное.

from fractions import Fraction


def print_operations(__first: str, __second: str) -> None:
    print(f'{__first} + {__second} = {Fraction(__first) + Fraction(__second)}')
    print(f'{__first} - {__second} = {Fraction(__first) - Fraction(__second)}')
    print(f'{__first} * {__second} = {Fraction(__first) * Fraction(__second)}')
    print(f'{__first} / {__second} = {Fraction(__first) / Fraction(__second)}')


def solution() -> None:
    print_operations(input(), input())


if __name__ == '__main__':
    solution()
