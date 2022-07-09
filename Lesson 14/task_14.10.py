# Напишите программу, которая рисует правильную пятиконечную звезду.


import turtle


def star(__length: int, __count: int) -> None:
    angle = 180 / __count
    for _ in range(__count):
        turtle.forward(__length)
        turtle.right(180 - angle)


def solution() -> None:
    length = 100
    count = 5
    star(length, count)
    input()


if __name__ == '__main__':
    solution()
