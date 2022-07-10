# Напишите программу для рисования паутины в соответствии с примером. Программа должна считывать количество лучей паутины, число n.

import turtle


def ray(__length: int) -> None:
    turtle.forward(__length)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(__length)
    turtle.left(180)



def star(__length: int, __count: int) -> None:
    angle = 360 / __count
    turtle.dot(10)
    for _ in range(__count):
        ray(__length)
        turtle.left(angle)


def solution() -> None:
    count = 10
    length = 100
    star(length, count)
    input()


if __name__ == '__main__':
    solution()