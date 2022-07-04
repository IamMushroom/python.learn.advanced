# Лотерейный билет содержит 7 чисел из диапазона от 1 до 49 (включительно).
#
# Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
# Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.

from random import randint


def generate_numbers() -> None:
    result = set()
    while len(result) < 7:
        result.add(randint(1, 49))

    print(*sorted(result))


def solution() -> None:
    generate_numbers()


if __name__ == '__main__':
    solution()
