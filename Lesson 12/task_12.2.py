# Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 6 гранями.
# Программа принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на грани кубика (каждое на отдельной строке).

from random import *


def dice_throw(__count: int, __dice: int) -> None:
    for _ in range(__count):
        print(randint(1, __dice))


def solution() -> None:
    count = int(input())
    dice = 6
    dice_throw(count, dice)


if __name__ == '__main__':
    solution()
