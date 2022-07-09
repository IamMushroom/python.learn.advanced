# Напишите программу, которая рисует соты.

import turtle


def hexagon(__side: int) -> None:
    turtle.shape('turtle')
    for _ in range(6):
        turtle.forward(__side)
        turtle.left(60)


def honeycomb(__side: int) -> None:
    for _ in range(6):
        hexagon(__side)
        turtle.left(120)
        turtle.forward(__side)
        turtle.right(60)


def solution() -> None:
    honeycomb(int(input()))
    input()


if __name__ == '__main__':
    solution()
