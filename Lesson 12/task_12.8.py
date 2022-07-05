# Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке.
# Обратите внимание, вы должны придерживаться следующих условий:
#
# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 7 цифр;
# все 100 лотерейных билетов должны быть различными.

from random import randint


def generate_numbers(__count: int) -> None:
    result = set()
    while len(result) < __count:
        result.add(randint(1000000, 9999999))
    print(*result, sep='\n')


def solution() -> None:
    count = 100
    generate_numbers(count)


if __name__ == '__main__':
    solution()
