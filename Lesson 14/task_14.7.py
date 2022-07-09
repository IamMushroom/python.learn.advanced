# Напишите программу, которая рисует ромб с углами 60 и 120 градусов.

import turtle


def rhombus(__side: int, __small_angle: int) -> None:
    turtle.shape('turtle')
    __big_angle = 180 - __small_angle
    for _ in range(2):
        turtle.forward(__side)
        turtle.left(__big_angle)
        turtle.forward(__side)
        turtle.left(__small_angle)


def solution() -> None:
    angle = 60
    rhombus(int(input()), 60)
    input()


if __name__ == '__main__':
    solution()
