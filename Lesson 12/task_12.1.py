# Напишите программу, которая с помощью модуля random моделирует броски монеты.
# Программа принимает на вход количество попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке).

from random import *


def flip_coin(__count: int) -> None:
    for _ in range(__count):
        if randint(0, 1):
            print('Орел')
        else:
            print('Решка')


def solution() -> None:
    count = int(input())
    flip_coin(count)


if __name__ == '__main__':
    solution()
