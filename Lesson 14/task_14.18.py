# Напишите программу, которая рисует черепашью спираль в соответствии с образцом.

import turtle


def helix(__start: int, __coil: int) -> None:
    __side = __start
    turtle.shape('turtle')
    turtle.penup()
    for _ in range(__coil):
        turtle.right(28)
        turtle.forward(__side)
        turtle.stamp()
        __side += __start


def solution() -> None:
    start = 2
    coil = 100
    helix(start, coil)
    input()


if __name__ == '__main__':
    solution()
