# Напишите программу, которая рисует звезду, показанную на рисунке. 
# Такую звезду можно создать из двух треугольников. 
# Однако их невозможно нарисовать непрерывной линией, поэтому перо нужно будет поднять для перехода ко второму треугольнику.

import turtle

def star(__side: int) -> None:
    turtle.goto(__side, 0)
    turtle.goto(__side // 2, __side)
    turtle.goto(0, 0)
    turtle.penup()
    turtle.goto(0, __side * 2/3)
    turtle.pendown()
    turtle.goto(__side, __side * 2/3)
    turtle.goto(__side // 2, __side * -1/3)
    turtle.goto(0, __side * 2/3)



def solution() -> None:
    star(180)
    input()


if __name__ == '__main__':
    solution()