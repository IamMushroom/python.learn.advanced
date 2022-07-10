# Напишите программу, которая рисует циферблат часов в соответствии с образцом.

import turtle


def ray(__length: int) -> None:
    turtle.penup()
    turtle.forward(__length - 40)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(__length)
    turtle.left(180)



def star(__length: int, __count: int) -> None:
    angle = 360 / __count
    turtle.shape('turtle')
    for _ in range(__count):
        ray(__length)
        turtle.left(angle)


def solution() -> None:
    count = 12
    length = 100
    star(length, count)
    input()


if __name__ == '__main__':
    solution()