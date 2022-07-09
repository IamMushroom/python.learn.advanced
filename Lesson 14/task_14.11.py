# Напишите программу, которая рисует квадраты, чтобы создать узор, показанный на рисунке.

import turtle


def square(__side: int) -> None:
    for _ in range(4):
        turtle.left(90)
        turtle.forward(__side)


def figure(__start: int, __inc: int, __count: int) -> None:
    __side = __start
    for _ in range(__count):
        square(__side)
        __side += __inc


def solution() -> None:
    start = 100
    inc = 20
    count = 10
    figure(start, inc, count)
    input()


if __name__ == '__main__':
    solution()
