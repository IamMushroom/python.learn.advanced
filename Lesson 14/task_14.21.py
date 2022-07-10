# Напишите программу, которая рисует изображение в соответствии с образцом.

import turtle


def ray(__endX: int, __endY: int) -> None:
    turtle.pencolor('green')
    turtle.pendown()
    turtle.goto(__endX, __endY)
    turtle.pencolor('blue')
    turtle.dot(5)
    turtle.penup()
    turtle.goto(0, 0)


def figure(__count: int) -> None:
    __Y = -150
    __deltaX = 300 // __count
    __X = -150 + (__deltaX // 2)
    for _ in range(__count):
        ray(__X, __Y)
        __X += __deltaX
    turtle.color('red')
    turtle.dot(5)


def solution() -> None:
    count = 10
    figure(count)
    input()


if __name__ == '__main__':
    solution()
