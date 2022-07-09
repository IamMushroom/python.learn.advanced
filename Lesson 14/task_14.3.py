# Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.

import turtle

def draw_sqare(__side: int) -> None:
    turtle.shape('turtle')

    for _ in range(4):
        turtle.forward(__side)
        turtle.left(90)


def draw_fig() -> None:
    turtle.left(15)
    side = int(input())
    for _ in range(3):
        draw_sqare(side)
        turtle.left(30)
    
def solution() -> None:
    draw_fig()
    input()


if __name__ == '__main__':
    solution()