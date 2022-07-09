# Напишите программу, которая рисует правильный шестиугольник.

import turtle


def hexagon(__side: int) -> None:
    turtle.shape('turtle')
    for _ in range(6):
        turtle.forward(__side)
        turtle.left(60)


def solution() -> None:
    hexagon(int(input()))
    input()


if __name__ == '__main__':
    solution()
