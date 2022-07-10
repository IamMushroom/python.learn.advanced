# Напишите программу, которая рисует узор в соответствии с образцом.

from random import randrange
import turtle


def helix(__start: int, __coil: int) -> None:
    __side = __start
    turtle.shape('turtle')
    radius = 1
    for _ in range(__coil):
        red, green, blue = randrange(256), randrange(256), randrange(256)
        turtle.pencolor(red, green, blue)
        turtle.pensize(radius)
        radius += 1
        turtle.left(45)
        turtle.forward(__side)
        __side += __start


def solution() -> None:
    start = 2
    coil = 100
    turtle.colormode(255)
    helix(start, coil)
    input()


if __name__ == '__main__':
    solution()
