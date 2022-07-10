# Напишите программу, которая рисует прямоугольник с точкой в каждом углу

import turtle


def rectangle(__sideA: int, __sideB: int) -> None:
    radius = 10
    for _ in range(2):
        turtle.forward(__sideA)
        turtle.dot(radius)
        turtle.left(90)
        turtle.forward(__sideB)
        turtle.dot(radius)
        turtle.left(90)


def solution() -> None:
    rectangle(200, 100)


if __name__ == '__main__':
    solution()
