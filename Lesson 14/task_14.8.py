# Напишите программу, которая рисует снежинку из 10 ромбовв.

import turtle


def rhombus(__side: int, __small_angle: int) -> None:
    turtle.shape('turtle')
    __big_angle = 180 - __small_angle
    for _ in range(2):
        turtle.forward(__side)
        turtle.left(__small_angle)
        turtle.forward(__side)
        turtle.left(__big_angle)


def snowflake(__side: int, __count: int) -> None:
    angle = 360 // __count
    rhombus_angle = 50
    for _ in range(__count):
        turtle.right(angle)
        rhombus(__side, rhombus_angle)
        turtle.left(angle * 2)


def solution() -> None:
    count = 6
    side = 100
    snowflake(side, count)
    input()


if __name__ == '__main__':
    solution()
