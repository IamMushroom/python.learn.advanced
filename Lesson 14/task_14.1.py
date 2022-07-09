# Напишите программу, которая рисует прямоугольник.

import turtle


def rectangle(width: int, height: int) -> None:
    turtle.shape('turtle')

    turtle.forward(width)
    turtle.right(90)

    turtle.forward(height)
    turtle.right(90)

    turtle.forward(width)
    turtle.right(90)

    turtle.forward(height)


def solution() -> None:
    rectangle(int(input()), int(input()))


if __name__ == '__main__':
    solution()
