# Напишите программу, которая рисует узор, показанный на рисунке.

import turtle


def helix(__start: int, __coil: int) -> None:
    __side = __start
    for _ in range(__coil):
        turtle.left(90)
        turtle.forward(__side)
        __side += __start


def solution() -> None:
    start = 2
    coil = 100
    helix(start, coil)
    input()


if __name__ == '__main__':
    solution()
