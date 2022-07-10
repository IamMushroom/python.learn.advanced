# Напишите программу, которая рисует пунктирную линию

import turtle


def dotted(__count: int, __radius: int) -> None:
    for _ in range(__count):
        turtle.dot(__radius)
        turtle.penup()
        turtle.forward(__radius * 2)
        turtle.pendown()


def solution() -> None:
    count = 8
    radius = 10
    dotted(count, radius)
    input()


if __name__ == '__main__':
    solution()
