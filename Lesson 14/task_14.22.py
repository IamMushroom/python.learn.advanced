# Напишите программу, которая рисует изображение символа олимпиады в соответствии с образцом.

import turtle


colors: dict[str, tuple[int, int]] = {
    'blue': (0, 0),
    'green': (182, -80),
    'black': (122, 0),
    'red': (242, 0),
    'yellow': (62, -80)
}


def rings() -> None:
    turtle.speed(10)
    turtle.pensize(4)
    for color in colors:
        turtle.penup()
        turtle.goto(colors[color])
        turtle.color(color)
        turtle.pendown()
        turtle.circle(60)


def solution() -> None:
    rings()
    input()


if __name__ == '__main__':
    solution()
