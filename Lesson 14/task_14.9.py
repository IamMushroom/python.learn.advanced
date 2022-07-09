# Напишите программу, которая рисует лучи звезды, показанной на рисунке.

from random import randrange
import turtle


def ray(__length: int) -> None:
    turtle.shape('turtle')
    for _ in range(2):
        turtle.forward(__length)
        turtle.left(180)


def star(__length: int, __count: int) -> None:
    angle = 360 / __count
    for _ in range(__count):
        ray(__length)
        turtle.left(angle)


def solution() -> None:
    count = 10
    length = 100
    star(length, count)
    input()


if __name__ == '__main__':
    solution()
