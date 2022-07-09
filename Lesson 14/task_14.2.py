# Напишите программу, которая рисует правильный треугольник.

import turtle


def triangle(side: int) -> None:
    turtle.shape('turtle')
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)


def solution() -> None:
    s = int(input())
    triangle(s)


if __name__ == '__main__':
    solution()
